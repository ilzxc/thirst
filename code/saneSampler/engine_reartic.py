from common import frange, interleave, collect, random, one, oneOf, ratio
from odotsetup import o
from query import filterCategories, getSamples

_ms = lambda time, total: time * total * 1000.

autocat = {
    'oboe': ['staccato'],
    'violin': ['staccato'],
    'viola': ['staccato'],
    'cello': ['staccato']
}

def reartic(pitch, time, instrument):
    """
    Rearticulation event generator.

    Returns an odot bundle for the rearticulation engine. API:
    /engine : "reartic"
    /samples : (list) -- a list of samples for polybuffer~
    /suffix : (string) -- filename suffix
    /time : (float) -- total time in seconds
    /events : (list of bundles) -- time-tagged bundles containing
              all of the articulations & envelopes

    This engine is different from others due to the fact that it
    plays multiple sounds, arranged in time. (For this reason, the
    current implementation does not generalize engines into a helper
    structure yet, which violates DRY and will be fixed in time.)
    """
    pass