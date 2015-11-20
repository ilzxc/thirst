from common import *
from instruments import *

def findIndices(target, coll):
    result = []
    for index, value in enumerate(coll):
        if value == target:
            result.append(index)
    return result

def grabIndices(indices, coll):
    result = map(lambda i: coll[i], indices)
    return result

def findPitches(pitch, coll):
    diffs = map(lambda note: pitch - note, coll)
    absdiffs = map(lambda diff: abs(diff), diffs)
    mindiff = min(absdiffs)
    return findIndices(mindiff, absdiffs)

def getSamples(pitch, instrument, categories):
    if type(categories) is not list:
        categories = [categories]
    result = []
    for category in categories:
        coll = SAMPLES[instrument][category]
        indices = findPitches(pitch, coll['midi'])
        for index in indices:
            entry = {}
            for subcat in coll:
                entry[subcat] = coll[subcat][index]
            result.append(entry)
    return result

def filterCategories(pitch, instrument, categories):
    diffs = map(lambda category: min(map(lambda midi: 
                abs(pitch - midi), SAMPLES[instrument][category]['midi'])), 
            categories)
    fit = filter(lambda d: abs(d[1]) < 7, collect(categories, diffs))
    return map(lambda elem: elem[0], fit)
