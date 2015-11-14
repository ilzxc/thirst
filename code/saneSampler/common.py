from random import random
from math import log

def lc(function, data):
	"""
	List Comprehension function application.

	If data received is a list, applies function to each member of
	the data array. Returns a new list. This library adheres to the
	following convention for function defitinions:

	_func(data) <-- single-value implementation
	func(data): return lc(_func, data) <-- client-friendly function
	"""
	if type(data) is list:
		result = []
		for datum in data:
			result.append(function(datum))
		return result
	return function(data)

# Math Functions: ----------------------------------------------------|

_ftom = lambda frequency: (12. / log(2.)) * log(frequency / 27.5) + 21.
_mtof = lambda midi: pow(2, (midi - 69.) / 12.) * 440.
_ratio = lambda factor: mtof(factor + 69.) / 440.

def ftom(frequency):
	return lc(_ftom, frequency)

def mtof(midi):
	return lc(_mtof, midi)

def ratio(factor):
	return lc(_ratio, factor)

def frange(*args):
	"""
	Floating-point range function
	"""
	if len(args) is 0:
		start, end, step = (0., 1., 1.)
	elif len(args) is 1:
		start, end, step = (0., args[0], 1.)
	elif len(args) is 2:
		start, end, step = (args[0], args[1], 1.)
	elif len(args) is 3:
		start, end, step = (args[0], args[1], args[2])
	else: print("Warning: too many args to frange")
	
	if (end - start) < 0:
		predicate = lambda a, b: a > b
		step = abs(step) * -1
	else:
		predicate = lambda a, b: a < b
		step = abs(step)
	
	i, result = (start, [])
	while predicate(i, end):
		result.append(i)
		i += step
	return result


# List Functions: ----------------------------------------------------|

def split(interleavedList, numLists = 2):
	"""
	Splits an interleaved list into multiple lists.

	Usage: freqs, amps = split(freqamps)
	Second argument specifies the number of lists:
	amps, times, curves = split(envelope, 3)
	"""
	if len(interleavedList) % numLists is not 0: return
	result = ()
	for i in range(0, numLists):
		result += (interleavedList[i::numLists],)
	return result


def interleave(*args):
	"""
	Interleaves lists into a single list.
	"""
	length = len(args[0])
	for i in range(1, len(args)):
		if len(args[i]) is not length:
			return None
	result = []
	for index, datum in enumerate(args[0]):
		result.append(datum)
		for i in range(1, len(args)):
			result.append(args[i][index])
	return result

def randomize(options):
	"""
	Returns a random item from a passed list.
	"""
	if len(options) is 0: return None
	return options[int(random() * len(options))]

def grab(indices, coll):
	"""
	"""
	result = []
	for index in indices: result.append(coll[ind])
	return result

















