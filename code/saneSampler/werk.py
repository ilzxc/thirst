samples1 = ['Ob-ord-A#3-ff.aif', 'Ob-ord-A#3-mf.aif', 'Ob-ord-A#3-pp.aif', 'Ob-ord-A#4-ff.aif', 'Ob-ord-A#4-pp.aif', 'Ob-ord-A#5-ff.aif', 'Ob-ord-A#5-mf.aif', 'Ob-ord-A#5-pp.aif', 'Ob-ord-A4-ff.aif', 'Ob-ord-A4-mf.aif', 'Ob-ord-A4-pp.aif', 'Ob-ord-A5-ff.aif', 'Ob-ord-A5-mf.aif', 'Ob-ord-A5-pp.aif', 'Ob-ord-A6-ff.aif', 'Ob-ord-A6-pp.aif', 'Ob-ord-B3-ff.aif', 'Ob-ord-B3-mf.aif', 'Ob-ord-B3-pp.aif', 'Ob-ord-B4-ff.aif', 'Ob-ord-B4-mf.aif', 'Ob-ord-B4-pp.aif', 'Ob-ord-B5-ff.aif', 'Ob-ord-B5-mf.aif', 'Ob-ord-B5-pp.aif', 'Ob-ord-C#4-ff.aif', 'Ob-ord-C#4-mf.aif', 'Ob-ord-C#5-ff.aif', 'Ob-ord-C#5-mf.aif', 'Ob-ord-C#5-pp.aif', 'Ob-ord-C#6-ff.aif', 'Ob-ord-C#6-mf.aif', 'Ob-ord-C#6-pp.aif', 'Ob-ord-C4-ff.aif', 'Ob-ord-C4-mf.aif', 'Ob-ord-C4-pp.aif', 'Ob-ord-C5-ff.aif', 'Ob-ord-C5-mf.aif', 'Ob-ord-C5-pp.aif', 'Ob-ord-C6-ff.aif', 'Ob-ord-C6-mf.aif', 'Ob-ord-C6-pp.aif', 'Ob-ord-D#4-ff.aif', 'Ob-ord-D#4-mf.aif', 'Ob-ord-D#4-pp.aif', 'Ob-ord-D#5-ff.aif', 'Ob-ord-D#5-mf.aif', 'Ob-ord-D#5-pp.aif', 'Ob-ord-D#6-ff.aif', 'Ob-ord-D#6-mf.aif', 'Ob-ord-D#6-pp.aif', 'Ob-ord-D4-ff.aif', 'Ob-ord-D4-mf.aif', 'Ob-ord-D4-pp.aif', 'Ob-ord-D5-ff.aif', 'Ob-ord-D5-mf.aif', 'Ob-ord-D5-pp.aif', 'Ob-ord-D6-mf.aif', 'Ob-ord-D6-pp.aif', 'Ob-ord-E4-ff.aif', 'Ob-ord-E4-mf.aif', 'Ob-ord-E5-ff.aif', 'Ob-ord-E5-mf.aif', 'Ob-ord-E5-pp.aif', 'Ob-ord-E6-ff.aif', 'Ob-ord-E6-mf.aif', 'Ob-ord-E6-pp.aif', 'Ob-ord-F#4-ff.aif', 'Ob-ord-F#4-mf.aif', 'Ob-ord-F#4-pp.aif', 'Ob-ord-F#5-ff.aif', 'Ob-ord-F#5-mf.aif', 'Ob-ord-F#5-pp.aif', 'Ob-ord-F#6-ff.aif', 'Ob-ord-F#6-mf.aif', 'Ob-ord-F#6-pp.aif', 'Ob-ord-F4-ff.aif', 'Ob-ord-F4-mf.aif', 'Ob-ord-F4-pp.aif', 'Ob-ord-F5-ff.aif', 'Ob-ord-F5-mf.aif', 'Ob-ord-F5-pp.aif', 'Ob-ord-F6-ff.aif', 'Ob-ord-F6-mf.aif', 'Ob-ord-F6-pp.aif', 'Ob-ord-G#4-ff.aif', 'Ob-ord-G#4-mf.aif', 'Ob-ord-G#4-pp.aif', 'Ob-ord-G#5-ff.aif', 'Ob-ord-G#5-mf.aif', 'Ob-ord-G#5-pp.aif', 'Ob-ord-G#6-ff.aif', 'Ob-ord-G#6-mf.aif', 'Ob-ord-G#6-pp.aif', 'Ob-ord-G4-ff.aif', 'Ob-ord-G4-pp.aif', 'Ob-ord-G5-ff.aif', 'Ob-ord-G5-mf.aif', 'Ob-ord-G5-pp.aif', 'Ob-ord-G6-ff.aif', 'Ob-ord-G6-mf.aif', 'Ob-ord-G6-pp.aif']



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

def midiffs(target, notes):
        result = []
        for note in notes: result.append(abs(target - note))
        return result

def mindex(diffs):
    return diffs.index(min(diffs))

def getClosestTranspose(target, notes):
    return target - notes[mindex(midiffs(target, notes))]

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

def convertToMidi(notesPresent):
    if type(notesPresent) is list:
        result = []
        for note in notesPresent:
            result.append(noteToMidi(note))
        return result
    else:
        return noteToMidi(notesPresent)

def determineNotes(fileStrings):
    nonAccidentals = ['E', 'B']
    withAccidentals = ['A', 'C', 'D', 'F', 'G']
    octaves = [2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    for fileString in fileStrings:
        for note in nonAccidentals:
            for octave in octaves:
                test = note + str(octave)
                if fileString.find(test) is not -1:
                    result.append(test)
        for note in withAccidentals:
            for octave in octaves:
                testWithout = note + str(octave)
                testWith = note + '#' + str(octave)
                if fileString.find(testWithout) is not -1:
                    result.append(testWithout)
                if fileString.find(testWith) is not -1:
                    result.append(testWith)
    return result

def findDynamic(dynamic, fileStrings):
    result = []
    for filename in fileStrings:
        if filename.find(dynamic) is not -1:
            result.append(filename)
    return result

def targetNote(midi):
    midi = int(midi)
    names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    noteNum = midi % 12
    octave = midi / 12 - 1
    return names[noteNum] + str(octave)

def closestNote(noteString, fileStrings):
    for filename in fileStrings:
        if filename.find(noteString) is not -1:
            return (filename, 0)
    # string not found
    midiTarget = convertToMidi(noteString)
    notesMidi = convertToMidi(determineNotes(fileStrings))
    closest = mindex(midiffs(midiTarget, notesMidi))
    transpose = midiTarget - notesMidi[closest]
    return (fileStrings[closest], transpose)
