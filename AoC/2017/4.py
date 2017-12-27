def solve1(instring):
    valids = 0
    for line in instring.split("\n"):
        words = line.split(" ")
        #print words
        matches = 0
        for iword in words:
            for jword in words:
                if iword == jword:
                    matches += 1
                    #print iword, jword
        #print matches, " vs ", len(words)
        if matches == len(words):
            valids += 1
    return valids

def solve2(instring):
    valids = 0
    for line in instring.split("\n"):
        words = line.split(" ")
        #print words
        matches = 0
        for iword in words:
            for jword in words:
                if sorted(iword) == sorted(jword):
                    matches += 1
                    #print iword, jword
        #print matches, " vs ", len(words)
        if matches == len(words):
            valids += 1
    return valids


tests = ''
with open('4in.txt', 'r') as myfile:
    tests = myfile.read()

print solve1(tests)
print solve2(tests)
