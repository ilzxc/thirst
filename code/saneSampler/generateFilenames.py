import os, re
from common import *

"""
Sample categories (named after orchidee folder names) for building a large
dictionary to be used throughout the application.
"""

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
	'dynamics': [
		'ordinario',
		'vibrato',
		'discolored-fingering',
		'flatterzunge',
		'harmonic-fingering',
		'staccato',
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
	'dynamics': [
		'artificial-harmonic',
		'artificial-harmonic-tremolo',
		'col-legno-tratto',
		'crushed-to-ordinario',
		'non-vibrato',
		'ordinario',
		'ordinario-to-crushed',
		'ordinario-to-sul-ponticello',
		'ordinario-to-sul-tasto',
		'ordinario-to-tremolo',
		'pizzicato-l-vib',
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
	'dynamics': [
		'artificial-harmonic',
		'artificial-harmonic-tremolo',
		'col-legno-tratto',
		'crushed-to-ordinario',
		'non-vibrato',
		'ordinario',
		'ordinario-to-crushed',
		'ordinario-to-sul-ponticello',
		'ordinario-to-sul-tasto',
		'ordinario-to-tremolo',
		'pizzicato-l-vib',
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
	'dynamics': [
		'artificial-harmonic',
		'artificial-harmonic-tremolo',
		'col-legno-tratto',
		'crushed-to-ordinario',
		'non-vibrato',
		'ordinario',
		'ordinario-to-crushed',
		'ordinario-to-sul-ponticello',
		'ordinario-to-sul-tasto',
		'ordinario-to-tremolo',
		'pizzicato-l-vib',
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

#---------------------------------------------------------------------------|

"""
Regular expressions for extracting string tokens from sample names:
"""
_applyre = lambda regexp, string: re.search(regexp, string).group(0)[1:-1]
def applyre(regexp, string):
	return lc(lambda s: _applyre(regexp, s), string)

"""
String number casts the first character of the string number token to int:
"""
_strnum = lambda string: int(string[0])
strnum = lambda string: lc(_strnum, string)

"""
Note string to midi number:
"""
def _ntom(note):
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

ntom = lambda note: lc(_ntom, note)

"""
Expressions for extracting note names (A7, G#5, etc), string numbers, dynamics:
"""
notename = r'-[A-G](#[0-9]|[0-9])[-\.]'
stringnum = r'-[1-4]c[-\.]'
dynamic = r'-(ff|f|mf|mp|p|pp)[-\.]'

"""
Script:
"""
result = {}

for instrument in instruments:
	print('processing {0}:'.format(instrument))
	using = instruments[instrument]
	categorySamples = {}
	for category in using['categories']:
		print('    category {0}'.format(category))
		cmd = 'ls -1 {path}/{category}/samples'.format(path = using['path'], category = category)
		samples = os.popen(cmd).read().split('\n')
		samples = samples[0:-1] # cut the empty \n from the end
		categorySamples[category] = {
			'files' : samples,
			'midi' : ntom(applyre(notename, samples))
		}
		if category in using['dynamics']:
			categorySamples[category]['dynamics'] = applyre(dynamic, samples)
		if using['name'] != 'oboe':
			categorySamples[category]['string'] = strnum(applyre(stringnum, samples))
	result[using['name']] = categorySamples;

f = open('instruments.py', 'w')
f.write('SAMPLES = ' + str(result) + '\n')
f.close()
