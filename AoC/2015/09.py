from itertools import permutations

sample1='''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141'''

def readinput(intext):
    locations = {}
    for line in intext:
        split = line.split()
        locationa = split[0]
        locationb = split[2]
        distance = (int)(split[-1])
        if locationa not in locations:
            locations[locationa] = {}
        if locationb not in locations:
            locations[locationb] = {}
        locations[locationa][locationb] = distance
        locations[locationb][locationa] = distance
    return locations


def solve1(intext):
    distances = readinput(intext)
    #print distances
    path = []
    mindistance = 10000000
    for permutation in permutations(distances):
        distance = 0
        for location in range(len(permutation)-1):
            distance += distances[permutation[location]][permutation[location+1]]
        if distance < mindistance:
            path = permutation
            mindistance = distance
    print path
    return mindistance

def solve2(intext):
    distances = readinput(intext)
    #print distances
    path = []
    maxdistance = 0
    for permutation in permutations(distances):
        distance = 0
        for location in range(len(permutation)-1):
            distance += distances[permutation[location]][permutation[location+1]]
        if distance > maxdistance:
            path = permutation
            maxdistance = distance
    print path
    return maxdistance


with open('inputs/09in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')

#print tests

print solve1(tests)
print solve2(tests)
