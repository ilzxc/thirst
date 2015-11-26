from common import frange, interleave, collect, random, one, oneOf, ratio
from odotsetup import o
from query import filterCategories, getSamples

_ms = lambda time, total: time * total * 1000.

autocat = {
    'oboe': ['staccato'],
    'violin': ['staccato'],
    'viola': ['staccato'],
    'cello': ['staccato']
}

def rapids_time(chord, time):
    """
    For rapid play, we create a rapid passage based on a number of
    notes in the chord.
    """
    bpm = random() * 40. + 60.
    tuplet = one([5, 6, 7, 4, 5, 6, 7])
    time_between_events = 60. / (bpm * tuplet)
    time_total = tuplet * time_between_events
    if time_total > time:
        time = time_total
    event_times = frange(0., time_total, time_between_events)
    return (time_between_events, time)

def rapids(chord, time, instrument):
    """
    Rapids event generator.

    Returns an odot bundle for the rapids engine. API:
    /engine : "rapids"
    /instrument : (string) -- instrument used
    /samples : (list) -- a list of samples for polybuffer~
    /suffix : (string) -- filename suffix
    /time : (float) -- total time in seconds
    /events : (list of bundles) -- bundles containing all of the
              information to play back a list of samples, rapidly.
    """
    # Figure out event times and update time if necessary:
    event_times, time = rapids_time(chord, time)

    # Figure out useful articulation categories:
    categories = []
    for pitch in chord:
        categories.append(filterCategories(pitch, instrument, autocat[instrument]))

    # create a dictionary of sound queries to be resolved by getSamples:
    soundqueries = [{'pitch' : elem[0], 'artic': elem[1]} for elem in collect(chord, categories)
                    if not(not elem[1])] # discard impossible notes (empty category)
    
    # execute the query, giving us the samples we'd need:
    seqfiles = [one(getSamples(sq['pitch'], instrument, sq['artic'])) for sq in soundqueries]
    
    # determine transposition ratios for sample playback:
    #correct = [pitch - ratio(sample['midi']) for sample in seqfiles]
    correct = [ratio(pair[0]['pitch'] - pair[1]['midi']) for pair in collect(soundqueries, seqfiles)]

    # filter redundant files:
    filenames = [e for e in set([sample['files'] for sample in seqfiles])]

    # determine the index of sample playback in polybuffer~:
    fileindices = [filenames.index(filename) + 1 for filename in [sq['files'] for sq in seqfiles]]

    # construct bundle:
    oengine = o.message('/engine', 'rapids')
    oinstr = o.message('/instrument', instrument)
    osamp = o.message('/samples', filenames)
    osuffix = o.message('/suffix', '_' + instrument + '_rapids.wav')
    otime = o.message('/time', time)
    events = []
    for index, value in enumerate(fileindices):
        opitch = o.message('/pitch', correct[index])
        obuffer = o.message('/buffer', instrument + '.rapids.' + str(value))
        oeventtime = o.message('/event/time', event_times * index + 0.05)
        events.append(o.bundle(messages = [opitch, obuffer, oeventtime]))
    oevents = o.message('/events', events)
    return o.bundle(messages = [oengine, oinstr, osamp, osuffix, otime, oevents])
