from common import *
from odotsetup import *
from query import *

_ms = lambda time, total: time * total * 1000.

instruments = ['violin', 'viola', 'cello']

autocat = {
    'violin': [
        'artificial-harmonic',
        'artificial-harmonic-tremolo',
        'col-legno-tratto',
        'non-vibrato',
        'ordinario',
        'ordinario-to-sul-ponticello',
        'ordinario-to-sul-tasto',
        'ordinario-to-tremolo',
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
        'non-vibrato',
        'ordinario',
        'ordinario-to-sul-ponticello',
        'ordinario-to-sul-tasto',
        'ordinario-to-tremolo',
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
        'non-vibrato',
        'ordinario',
        'ordinario-to-sul-ponticello',
        'ordinario-to-sul-tasto',
        'ordinario-to-tremolo',
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

def amp_in_out(time):
    """
    An AHD envelope.

    Attack (in the first 75 percent of the time)
    Hold @ sustain value (20 percent of the time)
    Sustain value is in between .5 and 1.
    Decay to 0. for the time remaining
    """
    ms = lambda t: _ms(t, time)
    attack_time = random() * .55 + .2
    sustain_val = random() * .5 + .5
    hold_time = random() * .2
    decay_time = 1. - attack_time - hold_time
    dest = [0., sustain_val, sustain_val, 0.]
    times = [0., ms(attack_time), ms(hold_time), ms(decay_time)]
    curves = [1., window(.75), 1., window(.75)]
    return interleave(dest, times, curves)

def amp_in(time):
    """
    A double-attack crescendo.
    """
    ms = lambda t: _ms(t, time)
    first_time = random() * .35 + .2
    second_time = random() * .3 + .2
    decay_time = 1 - first_time - second_time
    first_val = random() * .4 + .4
    dest = [0., first_val, 1., 0.]
    times = [0., ms(first_time), ms(second_time), ms(decay_time)]
    curves = [1.] + window([.75, .75, .75])
    return interleave(dest, times, curves)

def amp_out(time):
    """
    A double-decay diminuendo.
    """
    dest, times, curves = split(amp_in(time), 3)
    return interleave(dest[-1::-1], [0.] + times[-1:0:-1], curves)

def pitch_peak(time, correct):
    """
    A triangle-wave-like pitch shift.

    Moves up / down from no-transposition and returns to normal.
    Guaranteed to reach its destination within the first 75% of
    the time requested.
    """
    ms = lambda t: _ms(t, time)
    trans = ratio(window(2.) + correct)
    origin = ratio(correct)
    attack_time = random() * .75 + .2
    decay_time = 1. - attack_time
    dest = [origin, trans, origin]
    times = [0., ms(attack_time), ms(decay_time)]
    curves = [1.] + window([.75, .75])
    return interleave(dest, times, curves)

def pitch_unidir(time, correct):
    """
    Unidirectional pitch-shift into a specified pitch.

    Starts at most 3 semitones away from the desired pitch.
    """
    trans = ratio(window(3.) + correct)
    origin = ratio(correct)
    return interleave([trans, origin], [0., time * 1000], [1, window(.75)])

def pitch_cross(time, correct):
    """
    Shifts up then down (or down then up), before returning to
    the original pitch of the sample.
    """
    ms = lambda t: _ms(t, time)
    _ts = lambda: random() * .33 + .1
    shifts = window([2., 2.])
    if (shifts[0] * shifts[1]) > 0:
        shifts[one([0, 1])] *= -1
    trans = []
    for s in shifts:
        trans.append(s + correct)
    trans = ratio(trans)
    first = _ts()
    second = 1 - _ts() - first
    decay = 1. - (first + second)
    origin = ratio(correct)
    dest = [origin] + trans + [origin]
    times = [0., ms(first), ms(second), ms(decay)]
    curves = [1.] + window([.75, .75, .75])
    return interleave(dest, times, curves)

def moans(pitch, time, instrument = None, categories = None):
    """
    Engine Main.

    Returns an odot bundle for the moans engine. API:
    /samples : (string) -- a sample to use
    /time : (float) -- total time in seconds
    /pitch : (list) -- curve~ list for transposition ratios
    /amp : (list) -- curve~ list for amplitude envelope

    Upon receipt, engine queues /samples & executes envelopes
    """
    if instrument is None:
        instrument = one(['violin', 'viola', 'cello'])
    elif type(instrument) is list:
        instrument = one(instrument)        
    if categories is None:
        categories = one(autocat[instrument])
    elif type(categories) is list:
        categories = one(categories)

    query = one(getSamples(pitch, instrument, categories))
    correct = pitch - query['midi']
    sample = query['files']

    oengine = o.message('/engine', 'moan')
    osamp = o.message('/samples', sample)
    ofilename = o.message('/suffix', '_' + instrument + '_moan.wav')
    otime = o.message('/time', time)
    opitch = o.message('/pitch', one([pitch_peak, pitch_unidir, pitch_cross])(time, correct))
    oamps = o.message('/amp', one([amp_in_out, amp_in, amp_out])(time))

    return o.bundle(messages = [oengine, osamp, ofilename, otime, opitch, oamps])


