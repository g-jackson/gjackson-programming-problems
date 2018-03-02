from itertools import combinations, permutations
from operator import mul

sample1='''1
2
3
4
5
7
8
9
10
11'''

def splitter(weights, split, maxsize=0, minsize=0):
    if maxsize == 0:
        maxsize = len(weights)

    combos = []
    for i in range(minsize,maxsize+1):
        for j in combinations(weights,i):
            if sum(j) == split:    
                combos.append(list(j))
    return combos




# Very long runtime
def solve1(intext):
    weights =  map(int, intext)[::-1]
    maxmiddle = len(weights)/3
    split = sum(weights)/3
    print weights, split, maxmiddle
    middlecombos = splitter(weights, split, maxsize=maxmiddle)
    minpackages = len(weights)
    minqe = reduce(mul, weights, 1)
    smallest = []
    counter = 0
    print len(middlecombos)
    for mcombo in middlecombos:
        print counter
        counter += 1
        lremaining = [i for i in weights if i not in mcombo]
        leftcombos = splitter(lremaining,split, maxsize=(len(weights)-(len(mcombo)))/2,minsize=len(mcombo))
        for lcombo in leftcombos:
            rcombo = [i for i in weights if i not in mcombo and i not in lcombo]
            #print mcombo, lcombo, rcombo
            combo = (mcombo, lcombo, rcombo)
            if len(combo[0]) <= minpackages:
                minpackages = len(combo[0])
                product = reduce(mul, combo[0], 1)
                if product < minqe:
                    minqe = product
                    smallest = combo
                    print "minqe:", minqe

    print smallest, minqe, minpackages
    return minqe


def solve2(intext):
    weights =  map(int, intext)[::-1]
    groups = 4
    split = sum(weights)/groups
    for i in range(len(weights)):
        qes = [reduce(mul, c) for c in combinations(weights, i) if sum(c) == split]
        # Assuming we can generate three more even groups with remaining gifts 
        if len(qes) != 0:
            return min(qes)



with open('inputs/24in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
#print solve1(tests)
print solve2(tests)
