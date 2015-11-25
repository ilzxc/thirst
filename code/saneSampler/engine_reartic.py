from common import frange, interleave, collect, random, window, one, oneOf, ratio
from odotsetup import o
from query import filterCategories, getSamples
from engine_moans import amp_in_out

_ms = lambda time, total: time * total * 1000.

autocat = {
    'oboe': [
        'ordinario',
        'vibrato',
        'crescendo',
        'decrescendo',
        'discolored-fingering',
        'flatterzunge',
        'harmonic-fingering',
        'staccato',
        'sforzando',
        'lip-glissando'
    ],
    'violin': [
        'artificial-harmonic',
        'artificial-harmonic-tremolo',
        'col-legno-tratto',
        'crescendo',
        'crescendo-to-decrescendo',
        'crushed-to-ordinario',
        'decrescendo',
        'non-vibrato',
        'ordinario',
        'ordinario-to-crushed',
        'ordinario-to-sul-ponticello',
        'ordinario-to-sul-tasto',
        'ordinario-to-tremolo',
        'pizzicato-l-vib',
        'sforzato',
        'staccato',
        'sul-ponticello',
        'sul-ponticello-to-ordinario',
        'sul-ponticello-to-sul-tasto',
        'sul-ponticello-tremolo',
        'sul-tasto',
        'sul-tasto-to-ordinario',
        'sul-tasto-to-sul-ponticello',
        'tremolo',
        'tremolo-to-ordinario'
    ],
    'viola': [
        'artificial-harmonic',
        'artificial-harmonic-tremolo',
        'col-legno-tratto',
        'crescendo',
        'crescendo-to-decrescendo',
        'crushed-to-ordinario',
        'decrescendo',
        'non-vibrato',
        'ordinario',
        'ordinario-to-crushed',
        'ordinario-to-sul-ponticello',
        'ordinario-to-sul-tasto',
        'ordinario-to-tremolo',
        'pizzicato-l-vib',
        'sforzato',
        'staccato',
        'sul-ponticello',
        'sul-ponticello-to-ordinario',
        'sul-ponticello-to-sul-tasto',
        'sul-ponticello-tremolo',
        'sul-tasto',
        'sul-tasto-to-ordinario',
        'sul-tasto-to-sul-ponticello',
        'sul-tasto-tremolo',
        'tremolo',
        'tremolo-to-ordinario'
    ],
    'cello': [
        'artificial-harmonic',
        'artificial-harmonic-tremolo',
        'col-legno-tratto',
        'crescendo',
        'crescendo-to-decrescendo',
        'crushed-to-ordinario',
        'decrescendo',
        'non-vibrato',
        'ordinario',
        'ordinario-to-crushed',
        'ordinario-to-sul-ponticello',
        'ordinario-to-sul-tasto',
        'ordinario-to-tremolo',
        'pizzicato-l-vib',
        'sforzato',
        'staccato',
        'sul-ponticello',
        'sul-ponticello-to-ordinario',
        'sul-ponticello-to-sul-tasto',
        'sul-ponticello-tremolo',
        'sul-tasto',
        'sul-tasto-to-ordinario',
        'sul-tasto-to-sul-ponticello',
        'sul-tasto-tremolo',
        'tremolo',
        'tremolo-to-ordinario'
    ]
}

def subdivide(time):
    """
    Subdivides a segment of time, returns number of subdivs

    Need to be tweaked to ensure that events aren't too long or too
    short overall. 
    """
    bpm = random() * 40. + 220.
    num_beats = time * bpm / 30.
    beats = lambda: int(random() * 11. + 1.) # 1 -- 11 beats
    events = [0.]
    while num_beats > 0:
        take_beats = beats()
        last_event = events[len(events) - 1]
        events.append(take_beats * (30. / bpm) + last_event)
        num_beats -= take_beats
    if events[len(events) - 1] > time:
        events[len(events) - 1] = time
    return events

def reartic_time(time):
    """
    For rearticulation, we compose the total timeline of the
    performance based on (a) a set of prolongations, and (b)
    a set of quick "interruption" articulations
    """
    events = subdivide(time)
    lengths = [events[i] - events[i - 1] for i in range(1, len(events))]
    return (events, lengths)

def env_uniform(etime):
    """
    Uniform cresendo or diminuendo;
    """
    dests = [0., random() * .1 + .05, random() * .25 + .75, 0.]
    times = [0., 30., etime * 1000. - 60., 30.]
    curves = [0.] + window([.85, .85]) + [0.]
    if random() < .5:
        return interleave(dests, times, curves)
    return interleave(dests[-1::-1], [0.] + times[-1:0:-1], curves)

def env_jagged(etime):
    """
    Jagged envelope:

    Picks at most 4, at least 2 events for each second of
    the event time. Each event is categorized by a random 
    amplitude value and time distribution w/ a curve.
    """
    dests = [0.]
    times = [0.]
    time_error = 0.
    loctime = etime
    while loctime > 0:
        if loctime > 1.:
            correct = 1
        else:
            correct = loctime
        numevents = int((random() * 3. + 2.) * loctime)
        dests += [random() for i in range(numevents)]
        time_add = [random() / numevents for i in range(numevents)]
        next_error = 1. - sum(time_add)
        if len(time_add) > 0:
            time_add[0] += time_error
        times += time_add
        time_error = next_error
        loctime -= 1.
    dests[len(dests) - 1] = 0.
    times[len(times) - 1] += etime - sum(times)
    times = [1000. * t for t in times]
    curves = [0.] + [window(.75) for i in range(1, len(dests) - 1)] + [0.]
    return interleave(dests, times, curves)


def reartic(pitch, time, instrument):
    """
    Rearticulation event generator.

    Returns an odot bundle for the rearticulation engine. API:
    /engine : "reartic"
    /samples : (list) -- a list of samples for polybuffer~
    /suffix : (string) -- filename suffix
    /time : (float) -- total time in seconds
    /events : (list of bundles) -- time-tagged bundles containing
              all of the articulations & envelopes

    This engine is different from others due to the fact that it
    plays multiple sounds, arranged in time. (For this reason, the
    current implementation does not generalize engines into a helper
    structure yet, which violates DRY and will be fixed in time.)
    """
    # event_times = subdivide(time) # for o.schedule
    event_times, event_lengths = reartic_time(time)
    categories = []
    for event in event_lengths:
        categories.append(filterCategories(pitch, instrument, autocat[instrument]))

    soundqueries = [{'pitch': pitch, 'artic': category} for category in categories
                    if not (not category)] # discard impossible notes
    seqfiles = [one(getSamples(sq['pitch'], instrument, sq['artic'])) for sq in soundqueries]
    correct = [ratio(pitch - sound['midi']) for sound in seqfiles]
    filenames = [e for e in set([sample['files'] for sample in seqfiles])]
    fileindices = [filenames.index(filename) + 1 for filename in [sq['files'] for sq in seqfiles]]
    event_times = [e + .05 for e in event_times]

    oengine = o.message('/engine', 'reartic')
    oinstr = o.message('/instrument', instrument)
    osamp = o.message('/samples', filenames)
    osuffix = o.message('/suffix', '_' + instrument + '_reartic.wav')
    otime = o.message('/time', time)
    events = []
    envfuncs = [env_uniform, env_jagged, amp_in_out]
    for index, value in enumerate(fileindices):
        opitch = o.message('/pitch', correct[index])
        obuffer = o.message('/buffer', instrument + '.reartic.' + str(value))
        oeventtime = o.message('/event/time', event_times[index])
        oamp = o.message('/envelope', one(envfuncs)(event_lengths[index]))
        events.append(o.bundle(messages = [opitch, obuffer, oeventtime, oamp]))
    oevents = o.message('/events', events)
    return o.bundle(messages = [oengine, oinstr, osamp, osuffix, otime, oevents])

