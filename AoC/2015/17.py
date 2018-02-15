from itertools import combinations
sample1='''20
15
10
5
5 '''

def solve1(intext):
    size = 150
    containers = []
    for line in intext:
        containers.append((int)(line))
    #print containers
    valid = []
    for i in range(len(containers)):
        combos = combinations(containers, i)
        for combo in combos:
            if sum(combo) == size:
                valid.append(combo)
    #print valid

    return len(valid) 

def solve2(intext):
    size = 150
    containers = []
    for line in intext:
        containers.append((int)(line))
    #print containers
    valid = []
    mincontainers = len(containers)
    for i in range(len(containers)):
        combos = combinations(containers, i)
        for combo in combos:
            if sum(combo) == size:
                if len(combo) < mincontainers:
                    mincontainers = len(combo)
                    valid = [combo]
                elif len(combo) == mincontainers:
                    valid.append(combo)
    #print valid
    return len(valid) 

with open('inputs/17in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
print solve1(tests)
print solve2(tests)
