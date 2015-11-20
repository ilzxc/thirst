from random import random
from math import log

def ftom(frequency):
    if type(frequency) is list:
        result = []
        for f in frequency:
            result.append((12. / log(2.)) * log(f / 27.5) + 21.)
        return result
    return (12. / log(2.)) * log(frequency / 27.5) + 21.

def mtof(midi):
    if type(midi) is list:
        result = []
        for m in midi:
            result.append(pow(2, (m - 69.) / 12.) * 440.)
        return result
    return pow(2, (midi - 69.) / 12.) * 440.

def split(freqAmps):
    freqs = freqAmps[::2]
    amps = freqAmps[1::2]
    return (freqs, amps)

def interleave(freqs, amps):
    assert len(freqs) is len(amps)
    result = []
    for i, f in enumerate(freqs):
        result.append(f)
        result.append(amps[i])
    return result

def interleaveEvents(freqs, amps):
    assert len(freqs) is len(amps)
    result = []
    for i, f in enumerate(freqs):
        result.append([f, amps[i]])
    return result

def getBehavior(descriptors):
    if len(descriptors) is 0: return None
    return descriptors[int(random() * len(descriptors))]

def getChord():
    test = [2801.955811, 0.333805, 1088.253418, 0.998441, 3694.234619, 0.247559, 2019.767944, 1.0, 1788.372559, 0.064024]
    f, a = split(test)
    n = ftom(f)
    return interleaveEvents(n, a)

chord = getChord()
descriptors = ['sustain', 'moan', 'rhythm', 'attack']
events = []

for d in descriptors:
    events.append([])

for event in chord:
    behavior = getBehavior(descriptors)
    events[descriptors.index(behavior)].append(event)
    descriptors.remove(behavior)
    print(str(behavior) + str(descriptors))

