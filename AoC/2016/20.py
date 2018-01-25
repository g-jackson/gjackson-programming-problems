from collections import OrderedDict
sample1='''5-8
0-2
4-7'''

def solve1(intext):
    intext = sorted(intext)
    inlist = []
    for line in intext:
        line = line.split('-')
        inlist.append(((int)(line[0]), (int)(line[1])))
    inlist = sorted(inlist, key=lambda x: x[1])
    lowest = 0
    for blocked in inlist:
        #print "lowest", lowest, "blocked range", blocked
        if lowest >= blocked[0]:
            if blocked[1] + 1 > lowest:              
                lowest = blocked[1] + 1
    return lowest


def solve2(intext):

    return 


with open('inputs/20in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')

print solve1(tests)
#print solve2(tests)
