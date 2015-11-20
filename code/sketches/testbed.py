from instruments import *
from math import log, floor

def round(num):
	return int(floor(num)) if num % 1 < 0.5 else int(floor(num + 1))

def ftom(frequency):
	return (12 / log(2)) * log(frequency / 27.5) + 21

def toMidi(freqs):
	result = []
	for f in freqs:
		result.append(round(ftom(f)))
	return result

def getSample(instrument, note, category):
	notes = samples[instrument][category + '_midi']
	index = notes.index(note)
	return samples[instrument][category][index]

chord = [1379.190186, 0.651179, 
		 1931.732422, 0.257724, 
		 2347.467041, 0.162339, 
		 3276.810059, 1.000000, 
		 3779.893555, 0.135515]
		 
notes = chord[0:len(chord):2]
midi = toMidi(notes)
amps = chord[1:len(chord):2]

oboeCategory = 'ordinario'
violinCategory = 'non-vibrato'
violaCategory = 'sul-tasto-tremolo'

print(getSample('oboe', midi[0], oboeCategory))
print(getSample('violin', midi[1], violinCategory))
print(getSample('viola', midi[2], violaCategory))