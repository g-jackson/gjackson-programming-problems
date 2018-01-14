import operator as op
import sys
sys.setrecursionlimit(1000)

sample1 ='''flqrgnkx'''

def encode(knot):
    outstring = ''
    for i in knot:
        raw = format(i, 'x')
        if len(raw) == 1:
            raw = '0'+raw
        outstring = outstring + raw
    return outstring

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

def hashcreate(intext):
    intext = [ord(c) for c in intext]
    intext.extend([17,31,73,47,23])
    #print intext
    listsize = 256
    stringlist = range(0,listsize)
    currentpos = 0
    skipsize = 0
    #print stringlist
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
    #print knot
    return encode(knot)

def createdisk(inlist):
    bits = ""
    for i in range(128):
        knotin = inlist+ '-' +  (str)(i)
        #print knotin
        knotout = hashcreate(knotin)
        #print knotout
        scale = 16 
        num_of_bits = 128
        bits = bits + bin(int(knotout, scale))[2:].zfill(num_of_bits) + "\n"    
    bits = bits[:-1]
    return bits

def solve1(inlist):
    return createdisk(inlist).count('1')

def colour(bits, counter, groups, i, j):
    #print i, j
    if (i >= 0) and (j >= 0) and (i < 128) and (j < 128) and ((i,j) not in groups):
        if bits[i][j] == '1':
            groups[(i,j)] = counter
            if (i+1, j) not in groups:
                colour(bits, counter, groups, i+1, j)
            if (i-1, j) not in groups:
                colour(bits, counter, groups, i-1, j)
            if (i, j+1) not in groups:
                colour(bits, counter, groups, i, j+1)
            if (i, j-1) not in groups:
                colour(bits, counter, groups, i, j-1)


def solve2(inlist):
    bits = createdisk(inlist)
    #print bits
    bits = bits.split('\n')
    counter = 0
    groups = {}
    for i in range(128):
        for j in range(128):
            if bits[i][j] == '1':
                if (i,j) not in groups:
                    colour(bits, counter, groups, i ,j)
                    counter = counter + 1

    return counter


test = "wenycdww"
#test = sample1

#print test
#print solve1(test)
print solve2(test)

