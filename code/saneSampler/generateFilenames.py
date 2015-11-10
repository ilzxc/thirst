import os
from werk import *

def getNote(sampleString):
	chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
	found = -1
	for char in chars:
		test = sampleString.find(char)
		if test is not -1:
			found = test
			break
	if found is not -1:
		sharp = sampleString[found + 1] is '#'
		if sharp: return sampleString[found : found + 3]
		else: return sampleString[found : found + 2]

def noteToMidi(note):
	noteDict = {
		'C' : 0,
		'D' : 2,
		'E' : 4,
		'F' : 5,
		'G' : 7,
		'A' : 9,
		'B' : 11
	}
	sharp = 1 if note[1] is '#' else 0
	octave = int(note[2]) if sharp is 1 else int(note[1])
	start = 12 * (octave + 1)
	return start + noteDict[note[0]] + sharp

oboe = {
	'name': 'oboe',
	'categories': [
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
	'path': '/Users/ilyarostovtsev/Documents/music/SOL/sounds/orchidee/Oboes/Oboe'
}

violin = {
	'name': 'violin',
	'categories': [
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
	'path': '/Users/ilyarostovtsev/Documents/music/SOL/sounds/orchidee/Strings/Violin'
}

viola = {
	'name': 'viola',
	'categories': [
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
	'path': '/Users/ilyarostovtsev/Documents/music/SOL/sounds/orchidee/Strings/Viola'
}

cello = {
	'name': 'cello',
	'categories': [
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
	'path': '/Users/ilyarostovtsev/Documents/music/SOL/sounds/orchidee/Strings/Violoncello'
}

instruments = {
	'oboe': oboe,
	'violin': violin,
	'viola': viola,
	'cello': cello
}

f = open('instruments.py', 'w')

result = {}

for instrument in instruments:
	using = instruments[instrument]
	categorySamples = {}
	for category in using['categories']:
		cmd = 'ls -1 {path}/{category}/samples'.format(path = using['path'], category = category)
		samples = os.popen(cmd).read().split('\n')
		samples = samples[0:len(samples) - 1] # cut the empty \n from the end
		entry = []
		for sample in samples:
			entry.append([sample, noteToMidi(getNote(sample))])
		categorySamples[category] = entry
	result[using['name']] = categorySamples;

f.write('samples = ' + str(result) + '\n')
f.close()