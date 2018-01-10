import pprint
sample1 ='''../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#'''

def readinput(inlist):
    twos = []
    threes = []
    for line in inlist:
        line = line.split(' => ')
        inrows = line[0].split('/')
        for i in range(len(inrows)):
            inrows[i] = list(inrows[i])
        outrows = line[1].split('/')
        for i in range(len(outrows)):
            outrows[i] = list(outrows[i])
        translation = [inrows, outrows]
        if len(inrows[0]) == 2:
            twos.append(translation)
        else:
            threes.append(translation)

    translations = [twos, threes]
    return translations

def findrotations(pattern):
    rotations = [pattern]
    pattern = zip(*pattern[::-1])
    for i in range(len(pattern)):
        pattern[i] = list(pattern[i])
    rotations.append(pattern)
    pattern = zip(*pattern[::-1])
    for i in range(len(pattern)):
        pattern[i] = list(pattern[i])
    rotations.append(pattern)
    pattern = zip(*pattern[::-1])
    for i in range(len(pattern)):
        pattern[i] = list(pattern[i])
    rotations.append(pattern)
    #print rotations
    return rotations    

def print2d(arrayin):
    print ''
    for i in arrayin:
        print ''.join(i)
    

def match(translations, inpattern):
    # Find if inpattern is 2x2 or 3x3 and compare to same size translations
    if len(inpattern[0]) == 2:
        patterns = translations[0]
    else:
        patterns = translations[1]

    # Get all rotations of inpattern
    rotations = findrotations(inpattern)

    # Compare translation patterns to all rotations of inpatterns to find match
    for pattern in patterns:
        for rotation in rotations:
            #print2d(pattern[0])
            #print2d(rotation)
            if rotation == pattern[0]:
                translation = pattern[1]

    #print translation
    return translation

def solvesplit(translations, patterns):
    #print patterns
    for i in range(len(patterns)):
        pattern =  patterns[i]
        print2d(pattern)
        patterns[i] = match(translations, pattern)
    return patterns

def split(pattern):
    out = []
    if len(pattern[0]) % 2 == 0:
        split = 2
    else:
        split = 3

    return out

def combine(patterns):

    return patterns

def solve1(inlist):
    iterations = 1#5
    translations = readinput(inlist)
    pattern = [['#', '.', '.', '#'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['#', '.', '.', '#']]
    print2d(pattern)
    for i in range(iterations):
        print i
        print pattern
        splitlist = split(pattern)
        #print splitarray
        #splitarray =  solvesplit(translations, splitarray)
        #print splitarray
        #pattern = combine(splitarray)


    #print match(translations,[['.','.','.'],['.','.','.'],['.','.','#']])
    return #inlist


def solve2(inlist):
    return 


with open('inputs/21in.txt', 'r') as infile:
    test = infile.read()

test = sample1
test = test.split('\n')

#print test
print solve1(test)
#print solve2(test)

