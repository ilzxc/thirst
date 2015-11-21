"""
Query docstring here
"""

from common import collect
from instruments import SAMPLES

def findIndices(target, coll):
    """
    Find indices of matched targets in a collection.
    """
    return [index for index, value in enumerate(coll) if value == target]

def grabIndices(indices, coll):
    """
    Return elements of the collection at instances.
    """
    return [coll[i] for i in indices]

def findPitches(pitch, coll):
    """
    Returns indices of matching pitches in the collection.
    """
    absdiffs = [abs(pitch - note) for note in coll]
    return findIndices(min(absdiffs), absdiffs)

def getSamples(pitch, instrument, categories):
    """
    Get a list of samples matching pitches from a set of categories.
    """
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
    """
    Returns new list of categories that contain desired pitch.
    """
    diffs = [min([abs(pitch - midi) for midi in SAMPLES[instrument][category]['midi']]) for category in categories]
    return [elem[0] for elem in collect(categories, diffs) if elem[1] < 7]
    