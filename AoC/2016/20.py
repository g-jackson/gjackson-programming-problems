from collections import OrderedDict
sample1='''5-8
0-2
3-8'''

def solve1(intext):
    intext = sorted(intext)
    inlist = []
    for line in intext:
        line = line.split('-')
        inlist.append(((int)(line[0]), (int)(line[1])))
    inlist = sorted(inlist, key=lambda x: x[0])
    lowest = 0
    for blocked in inlist:
        #print "lowest", lowest, "blocked range", blocked
        if lowest >= blocked[0]:
            if blocked[1] + 1 > lowest:              
                lowest = blocked[1] + 1
    return lowest


def solve2(intext):
    intext = sorted(intext)
    inlist = []
    for line in intext:
        line = line.split('-')
        inlist.append(((int)(line[0]), (int)(line[1])))
    inlist = sorted(inlist, key=lambda x: x[0])
    #for line in inlist:
        #print line[0]
    total = 4294967296
    lowest = inlist[0][1]
    start = inlist[0][0]
    allowed = start
    for blocked in inlist:
        if blocked[0] > lowest:
            allowed = allowed + (blocked[0] - lowest) -1
            lowest = blocked[1]
        if blocked[1] > lowest:
            lowest = blocked[1]         
    return allowed


with open('inputs/20in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')

#print solve1(tests)
print solve2(tests)
