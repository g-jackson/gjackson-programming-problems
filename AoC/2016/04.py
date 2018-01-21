import re
from collections import Counter

sample1='''aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]'''



def solve1(intext):
    for line in intext:
        name = re.sub('-', '', line.split('[')[0][:-3])
        sector = line.split('[')[0][-3:]
        checksum = line.split('[')[1][0:5]
        counter = Counter(name)
        countsum = []
        while not len(countsum) != 5:
            thissize = counter[0][1]
            
        print name, sector, counter, checksum, 
    return 

def solve2(intext):

    return 


with open('inputs/04in.txt', 'r') as infile:
    tests = infile.read()

tests = sample1
tests = tests.split('\n')

print tests

print solve1(tests)
#print solve2(tests)
