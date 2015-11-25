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
from engine_reartic import reartic
from time import sleep

parse_line = lambda l: [float(x) for x in l[l.find(',') + 1 : l.find(';')].split()]

lowest_notes = {
    'oboe': 58,   # b-flat below middle C
    'violin': 55, # g below middle C
    'viola': 48,  # c below middle C
    'cello': 36   # c below viola c
}

check = lambda note: filter(lambda key: lowest_notes[key] <= note, lowest_notes)
intersect = lambda lhs, rhs: filter(lambda elem: elem in rhs, lhs)

def prepareChord(chord):
    """
    Takes in a chord as an interleaved list of freqs & amps;
    Returns a list of lists containing midi floats & amps.
    """
    freqs, amps = split(chord)
    return collect(ftom(freqs), amps)

chords = []

for i in range(0, 30):
    with open('../../solutions/Apeak' + str(i) + '.txt') as f:
        for line in f.readlines():
            chords.append(parse_line(line))

for chord in chords:
    notes = prepareChord(chord)
    instruments = ['oboe', 'violin', 'viola', 'cello']
    time = abs(window(4.)) + 2.
    note, notes = oneOf(notes)

    while len(instruments) > 0 and len(notes) > 0:
        bundles = []
        note, notes = oneOf(notes)
        possible_instruments = intersect(instruments, check(note))
        instrument = one(possible_instruments)
        instruments.remove(instrument)
        voiceTime = window(time) * .2 + time
        note_used = note[0]
        if one([0, 1]) is 0: 
            note_used = round(note_used)
        bundles.append(reartic(note_used, voiceTime, instrument))
        oscore = o.message('/score', bundles)
        file_prefix = prefix()
        oprefix = o.message('/prefix', file_prefix)
        otime = o.message('/time', time + 3.)
        result = o.bundle(messages = [oscore, otime, oprefix])
        f = open('./scores/' + file_prefix + '_score.txt', 'w')
        f.write(str(result))
        f.close()
        send(result)
        print(result)
        print('-' * 100)
        sleep(time * 2 + 3.)

print("Finished...")
