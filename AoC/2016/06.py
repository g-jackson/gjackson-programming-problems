from collections import Counter
import numpy as np


sample1='''eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar'''

def solve1(intext):
    rows = []
    for line in intext:
        rows.append(list(line))
    rows = np.array(rows)
    rows = np.rot90(rows,3)
    mostcommon = []
    for row in rows:
        counter = Counter(row)
        #print counter.most_common(1)[0][0]
        mostcommon.append(counter.most_common(len(counter))[-1][0]) 
    #print rows
    return ''.join(mostcommon)

def solve2(intext):
    rows = []
    for line in intext:
        rows.append(list(line))
    rows = np.array(rows)
    rows = np.rot90(rows,3)
    mostcommon = []
    for row in rows:
        counter = Counter(row)
        #print counter.most_common(1)[0][0]
        mostcommon.append(counter.most_common(1)[0][0]) 
    #print rows
    return ''.join(mostcommon)
    return 


with open('inputs/06in.txt', 'r') as infile:
    tests = infile.read()

tests = sample1
tests = tests.split('\n')
#print tests

print solve1(tests)
#print solve2(tests)
