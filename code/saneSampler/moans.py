from common import *
from udp import *
from odotsetup import *

window = lambda n = 1.: n * (random() * 2. - 1.) 

def amp_in_out(time):
    attack_time = random() * .55 + .2
    sustain = random() * .50 + .50
    hold_time = random() * .2
    decay_time= 1. - attack_time - hold_time
    return [0., 0., 1., 
            sustain, attack_time * time * 1000, window() * 0.75, 
            sustain, hold_time * time * 1000, 1., 
            0., decay_time * time * 1000, window() * 0.75]

def amp_in(time):
    pass

def amp_out(time):
    pass

def pitch_peak(time):
    trans = ratio(2.)
    attack_time = random() * .75 + .2
    decay_time = 1. - attack_time
    return [1., 0., 1.,
            trans, attack_time * time * 1000, window(),
            1., decay_time * time * 1000, window()]

def pitch_unidir(time):
    trans = ratio(3.)
    return[trans, 0., 1., 1., time * 1000, window()]

def pitch_cross(time):
    trans = [window(2.), window(2.)]
    if (trans[0] * trans[1]) > 0:
        trans[randomize([0, 1])] *= -1
    trans = ratio(trans)
    first = random() * .33 + .1
    second = 1. - (random() * .33 + .1) - first
    decay = 1. - (first + second)
    return [1., 0., 1.,
            trans[0], first * time * 1000, window() * .75,
            trans[1], second * time * 1000, window() * .75,
            1., decay * time * 1000, window() * .75]

def pitch_beats(time, open_string):
    pass

time = 3.1
t = o.message('/time', time * 1000)
amp = o.message('/amp', amp_in_out(time))
pitch = o.message('/pitch', pitch_cross(time))

send(o.bundle(messages = [amp, pitch, t]))