"""
	THIRST:

	Produces sound descriptors for chords used in the piece, to be sonified
	by THIRST Max Engines.

	Inputs: chord to be articulated;
	Outputs: a udp-bound odot bundle for different engines.
"""

from common import *
from odotsetup import *
from udp import send
from engine_moans import moans
from time import sleep
from thoughts2 import prefix

chords = [
	[2801.955811, 0.333805, 1088.253418, 0.998441, 3694.234619, 0.247559, 2019.767944, 1.000000, 1788.372559, 0.064024],
	[3165.476318, 0.985535, 806.581726, 1.000000, 3732.806396, 0.473814, 2530.415039, 0.316540, 1375.920288, 0.808892],
	[525.259705, 0.945358, 1136.167480, 0.362523, 2155.104980, 1.000000, 3452.213379, 0.184657, 3942.270508, 0.948462],
	[732.088623, 1.000000, 1712.914551, 0.209545, 2018.184326, 0.560162, 2800.334229, 0.825774, 3825.981201, 0.162353],
	[852.642944, 0.401350, 1227.326050, 1.000000, 1734.575073, 0.269507, 2073.365234, 0.937920, 2496.795410, 0.080503]
]

def prepareChord(chord):
    """
    Takes in a chord as an interleaved list of freqs & amps;
    Returns a list of lists containing midi floats & amps.
    """
    freqs, amps = split(chord)
    return collect(ftom(freqs), amps)

for chord in chords:
	notes = prepareChord(chord)
	instruments = ['violin', 'viola', 'cello']

	time = abs(window(4.)) + .3

	bundles = []

	while len(instruments) > 0:
		instrument, instruments = oneOf(instruments)
		note, notes = oneOf(notes)
		voiceTime = window(time) * .2 + time

		note_used = note[0]
		if one([0, 1]) is 0: note_used = round(note_used)

		bundles.append(moans(note_used, voiceTime, instrument))

	oscore = o.message('/score', bundles)
	file_prefix = prefix()
	oprefix = o.message('/prefix', file_prefix)
	result = o.bundle(messages = [oscore, oprefix])
	f = open(file_prefix + '_score.txt', 'w')
	f.write(str(result))
	f.close()
	send(result)
	sleep(time + 4.)

print("Finished...")
