from common import interleave, random, one, ratio
from odotsetup import o
from query import filterCategories, getSamples

_ms = lambda time, total: time * total * 1000.

instruments = ['oboe', 'violin', 'viola', 'cello']

autocat = {
    'oboe': [
        'staccato',
        'sforzando'
    ],
    'violin': [
        'pizzicato-l-vib',
        'sforzato',
        'staccato'
    ],
    'viola': [
        'pizzicato-l-vib',
        'sforzato',
        'staccato'
    ],
    'cello': [
        'pizzicato-l-vib',
        'sforzato',
        'staccato'
    ]
}

def amp_env(time):
    """
    A simple AHD envelope.

    20 ms ramp up, hold for most of the time, 20 ms 
    ramp down.
    """
    ms = lambda t: _ms(t, time)
    attack = decay = 20 # ms
    hold = ms(time) - 40 # ms
    sustain = random() * .5 + .5
    dest = [0., sustain, sustain, 0.]
    times = [0., attack, hold, decay]
    return interleave(dest, times)

def perc(pitch, time, instrument):
    """
    Engine Main.

    Returns an odot bundle for the perc engine. API:
    /engine : "perc"
    /samples: (string) -- a sample to use
    /suffix : (string) -- filename suffix
    /tmie : (float) -- total time in seconds
    /pitch : (float) -- transposition factor
    /amp : (list) -- line~ list for amplitude envelope
    """
    categories = autocat[instrument]

    categories = filterCategories(pitch, instrument, categories)
    if len(categories) is 0:
        return o.bundle()

    query = one(getSamples(pitch, instrument, categories))
    correct = pitch - query['midi']
    sample = query['files']

    oengine = o.message('/engine', 'perc')
    osamp = o.message('/samples', sample)
    ofilename = o.message('/suffix', '_' + instrument + '_perc.wav')
    otime = o.message('/time', time)
    opitch = o.message('/pitch', ratio(correct))
    oamps = o.message('/amp', amp_env(time))
    return o.bundle(messages = [oengine, osamp, ofilename, otime, opitch, oamps])
