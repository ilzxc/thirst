from random import random
from udp import *
from odotsetup import *

moan_categories = {
	'violin' : [],
	'viola' : [],
	'cello' : []
}

def mtof(n):
	return pow(2, (n - 69.0) / 12.0) * 440.

def curve(): return random() * 2. - 1.

def amp_in_out(time):
	attack_time = random() * .55 + .2
	sustain = random() * .50 + .50
	hold_time = random() * .2
	decay_time= 1. - attack_time - hold_time
	return [0., 0., 1., 
			sustain, attack_time * time * 1000, curve() * 0.75, 
			sustain, hold_time * time * 1000, 1., 
			0., decay_time * time * 1000, curve() * 0.75]

def amp_in(time):
	pass

def amp_out(time):
	pass

def pitch_peak(time):
	reference = mtof(60.0)
	trans = curve() * 2.
	ratio = mtof(60 + trans) / reference
	attack_time = random() * .75 + .2
	decay_time = 1. - attack_time
	return [1., 0., 1.,
			ratio, attack_time * time * 1000, curve(),
			1., decay_time * time * 1000, curve()]

def pitch_cross(time):
	pass

def pitch_beats(time, open_string):
	pass

time = 3.1
t = o.message('/time', time * 1000)
amp = o.message('/amp', amp_in_out(time))
pitch = o.message('/pitch', pitch_peak(time))

send(o.bundle(messages = [amp, pitch, t]))