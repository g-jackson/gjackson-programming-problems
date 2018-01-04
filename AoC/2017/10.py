sample1 = '''3,4,1,5'''

def flip(inlist, start, length):
    end = (start + length -1) % len(inlist)
    print start, end, length
    for i in range(length/2):
        endval = inlist[end]
        startval = inlist[start]
        inlist[start] = endval
        inlist[end] = startval
        start = (start+1) % len(inlist)
        end =  (end-1) % len(inlist)
    return inlist

def solve1(intext):
    listsize = 256
    stringlist = range(0,listsize)
    currentpos = 0
    skipsize = 0
    print stringlist
    for length in intext:
        flip(stringlist, currentpos, length)
        currentpos = (currentpos + length + skipsize) % listsize
        skipsize = skipsize + 1
        print currentpos, length, stringlist


    return stringlist[0]*stringlist[1] 

def solve2(intext):
    return 


with open('10in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1

tests = tests.split(',')
tests = map(int, tests)

print tests

print solve1(tests)
#print solve2(tests)
