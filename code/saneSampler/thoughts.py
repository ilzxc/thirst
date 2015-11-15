def prepareChord(chord):
    """
    Takes in a chord as an interleaved list of freqs & amps;
    Returns a list of lists containing midi floats & amps.
    """
    freqs, amps = split(chord)
    return collect(ftom(freqs), amps)


# Get a nested list of [note, amp] lists:
notes = prepareChord(chord)

# Define instruments you'd like to use:
instruments = ['oboe', 'violin', 'viola', 'cello']

# Determine the total time for the event:
time = 3.14159 # seconds

# Generate data to feed each instrument:
bundles = []
while len(instruments) > 0:
    # pick one of the instruments:
    instrument, instruments = oneOf(instruments)

    # pick one of the chord notes:
    note, notes = oneOf(notes)

    # pick an articulation type:
    artics = ['sustain', 'tremble', 'attack']
    if instrument != 'oboe': artics.append('moan')
    articulation = oneOf(arics)

    # pick samples:
    samples = fetchSample(articulation, note)

    # alter time slightly for the voice:
    voiceTime = window(time) * .2 + time

    # generate bundles:
    bundles.append(getEngine(articulation)(samples, voiceTime))

# union and send:
send(union(bundles))

"""
    TODO:

    1. fetchSample, as a function of articulation & note
    2. define engines for articulation types:
        * moan
        * sustain (with envelopes)
        * tremble (subtle rhythm)
        * rearticulate (rhythmic articulation)
        * attack (percussive staccato, pizz, sfz)

    fetchSample will always return an array of tuples
    containing sample name & transposition factor.
"""
