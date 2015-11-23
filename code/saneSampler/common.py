from random import random
from math import log
from time import localtime, clock

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
_window = lambda half = 1.: half * (random() * 2. - 1.) 

def ftom(frequency):
    """
    Frequency to Midi Number
    """
    return lc(_ftom, frequency)

def mtof(midi):
    """
    Midi Float to Frequency
    """
    return lc(_mtof, midi)

def ratio(factor):
    """
    Helper function for determining transposition ratios.
    Expects an argument as a midi float, returns the ratio for
    equal tempered transposition
    """
    return lc(_ratio, factor)

def window(half):
    """
    Returns values between -argument & argument. 
    """
    return lc(_window, half)

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
    
    predicate = lambda a, b: a < b
    step = abs(step)
    if (end - start) < 0:
        predicate = lambda a, b: a > b
        step *= -1  

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

def equalLengths(*args):
    """
    Verifies that the lenghs of lists passed as arguments
    are equal.
    """
    length = len(args[0])
    for i in range(1, len(args)):
        if len(args[i]) is not length:
            return False
    return True

def interleave(*args):
    """
    Interleaves lists into a single list.
    """
    if not equalLengths(args): return None
    result = []
    for index, datum in enumerate(args[0]):
        result.append(datum)
        for i in range(1, len(args)):
            result.append(args[i][index])
    return result

def collect(*args):
    """
    Similar to interleave, collects multiple lists into a
    list of lists. Unlike interleave, corresponding entries
    are collected into sublists, grouping heterogeous data 
    together.
    """
    if not equalLengths(args): return None
    result = []
    for index, datum in enumerate(args[0]):
        entry = [datum]
        for i in range(1, len(args)):
            entry.append(args[i][index])
        result.append(entry)
    return result

def oneOf(options):
    """
    Returns a random item from a passed list.

    In addition, randomize removes the item from a copy of 
    the list, and returns this (shorter) list as a second argument. 
    """
    if len(options) is 0: return (None, None)
    index = int(random() * len(options))
    copy = options[:index] + options[index + 1:]
    return (options[index], copy)

def one(options):
    """
    Similar to oneOf, but returns only the element.
    """
    if len(options) is 0: return None
    return options[int(random() * len(options))]

def grab(indices, array):
    """
    """
    result = []
    for index in indices: result.append(array[ind])
    return result

# File Functions -----------------------------------------------------|

def prefix():
    t = localtime()
    return "{0}{1}{2}{3}{4:.4f}".format(t.tm_mon, t.tm_mday,
                                        t.tm_hour, t.tm_min,
                                        t.tm_sec + clock())

