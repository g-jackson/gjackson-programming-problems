import operator as op
sample1 = '''3,4,1,5'''

def flip(inlist, start, length):
    end = (start + length -1) % len(inlist)
    #print start, end, length
    for i in range(length/2):
        endval = inlist[end]
        startval = inlist[start]
        inlist[start] = endval
        inlist[end] = startval
        start = (start+1) % len(inlist)
        end =  (end-1) % len(inlist)
    return inlist

def solve1(intext):
    intext = intext.split(',')
    intext = map(int, intext)
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

def encode(knot):
    outstring = ''
    for i in knot:
        raw = format(i, 'x')
        if len(raw) == 1:
            raw = '0'+raw
        outstring = outstring + raw
    return outstring

def solve2(intext):
    intext = [ord(c) for c in intext]
    intext.extend([17,31,73,47,23])
    listsize = 256
    stringlist = range(0,listsize)
    currentpos = 0
    skipsize = 0
    print stringlist
    for i in range(64):
        for length in intext:
            flip(stringlist, currentpos, length)
            currentpos = (currentpos + length + skipsize) % listsize
            skipsize = skipsize + 1
        #print stringlist

    knot = []
    for i in range(16):
        sparse = stringlist[i*16:((i+1)*16)]
        knot.append(reduce(op.xor, sparse))
    print knot
    return encode(knot)



with open('inputs/10in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1



print tests

#print solve1(tests)
print solve2(tests)
