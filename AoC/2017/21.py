import pprint
import numpy as np
import math
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
        translation = (np.array(inrows), np.array(outrows))

        if len(inrows[0]) == 2:
            twos.append(translation)
        else:
            threes.append(translation)

    translations = [twos, threes]
    return translations

def match(translations, inpattern):
    # Find if inpattern is 2x2 or 3x3 and compare to same size translations
    if len(inpattern[0]) == 2:
        patterns = translations[0]
    else:
        patterns = translations[1]

    # Get all rotations of inpattern
    rotations = []
    rotated = inpattern
    for i in range(4):
        rotated = np.rot90(rotated)
        rotations.append(rotated)
        rotations.append(np.flip(rotated,1))
    # Compare translation patterns to all rotations of inpatterns to find match
    match = []
    for pattern in patterns:
        for rotation in rotations:
            #print pattern[0]
            #print rotation
            #print "\n"
            if np.array_equal(pattern[0], rotation):
                match = pattern[1]
                #print "match"

    return match


def split(pattern):
    out = []
    if len(pattern[0]) % 2 == 0:
        split = 2
    else:
        split = 3
    for i in range(len(pattern)/split):
        for j in range(len(pattern)/split):
            out.append(pattern[(split*i):(split*i)+split,(split*j):split+(split*j)])
    return out

def combine(patterns):
    combinedx = []
    width = (int)(math.sqrt(len(patterns)))
    for i in range(len(patterns)/width):
        combinedx.append(np.concatenate(patterns[i*width:(i+1)*width],axis=1))
    #print combinedx
    combinedy = combinedx[0]
    for i in range(len(combinedx)-1):
        #print combinedy
        #print combinedx[i+1]
        combinedy = np.concatenate([combinedy, combinedx[i+1]],axis=0)
    #print combinedy
    return combinedy

def solve1(inlist):
    iterations = 5#5
    translations = readinput(inlist)
    
    print "Translations"
    '''
    for translation in translations:
        for size in translation:
            print size[0]
            print size[1]
    '''
    pattern = np.array([['.', '#', '.'],['.', '.', '#'], ['#', '#', '#']])
    #pattern = np.array([['#', '.', '.', '#'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['#', '.', '.', '#']])
    print pattern
    count = 0
    for i in range(iterations):
        splitlist = split(pattern)
        newpattern = []
        for subarray in splitlist:
            matched = match(translations,subarray)
            #print "Translating"
            #print subarray
            #print "To"
            #print matched
            newpattern.append(matched)

        pattern = combine(newpattern)
        print pattern
        count = 0
        for x in pattern:
            for y in x:
                count = count + y.count('#')
        print count

    return count


def solve2(inlist):
    return 


with open('inputs/21in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')

#print test
print solve1(test)
#print solve2(test)

