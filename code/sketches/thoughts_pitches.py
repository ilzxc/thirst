from common import *
from instruments import *

def findIndices(target, coll):
	result = []
	for index, value in enumerate(coll):
		if value == target:
			result.append(index)
	return result

def grabIndices(indices, coll):
	result = []
	for i in indices:
		result.append(coll[i])
	return result

def findPitches(pitch, coll):
	diffs = []
	for note in coll:
		diffs.append(pitch - note)
	absdiffs = []
	for diff in diffs:
		absdiffs.append(abs(diff))
	mindiff = min(absdiffs)
	return findIndices(mindiff, absdiffs)

def getSamples(pitch, instrument, categories):
	if type(categories) is not list:
		categories = [categories]
	result = []
	for category in categories:
		print(category)
		coll = SAMPLES[instrument][category]
		indices = findPitches(pitch, coll['midi'])
		for index in indices:
			entry = {}
			for subcat in coll:
				entry[subcat] = coll[subcat][index]
			result.append(entry)
	return result

