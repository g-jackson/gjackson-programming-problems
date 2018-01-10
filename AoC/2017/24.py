import string

sample1 = '''0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10'''

def createbridge(prev, pieces, start, bridges):
    weight = 0
    length = 0
    bridges.append(prev)
    #print prev
    for piece in pieces:
        pieces = list(pieces)
        thisweight = 0
        if piece[0] == start:
            #print "found", piece, "looking for", piece[1]
            pieces.remove(piece)
            newprev = "%s %s/%s" % (prev, piece[0], piece[1])
            thisweight = createbridge(newprev, pieces, piece[1], bridges) + piece[0] + piece[1]
        elif piece[1] == start:
            #print "found", piece, "looking for", piece[0]
            pieces.remove(piece)
            newprev = "%s %s/%s" % (prev, piece[1], piece[0])
            thisweight = createbridge(newprev, pieces, piece[0], bridges) + piece[0] + piece[1]
        if thisweight > weight:
            weight = thisweight
    return weight

def solve1(intext):
    start = 0
    pieces = []
    bridges = []
    for i in intext:
        #print i
        piece = ((int)(i.split('/')[0]),(int)(i.split('/')[1]))
        pieces.append(piece)
    #print pieces
    weight = createbridge("", pieces,start, bridges)
    return weight

def solve2(intext):
    maxweight = 0
    start = 0
    pieces = []
    bridges = []
    for i in intext:
        #print i
        piece = ((int)(i.split('/')[0]),(int)(i.split('/')[1]))
        pieces.append(piece)
    #print pieces
    weight = createbridge("", pieces, start, bridges)
    
    maxlength = 0
    maxweight = 0
    for bridge in bridges[1:]:
        weights = string.replace(bridge[1:], '/',' ')
        weights = weights.split(' ')
        if len(weights) > maxlength:
            maxlength = len(weights)
            bridgeweight = 0
            for weight in weights:
                bridgeweight = bridgeweight + (int)(weight)
            maxweight = bridgeweight
        if len(weights) == maxlength:
            bridgeweight = 0
            for weight in weights:
                bridgeweight = bridgeweight + (int)(weight)
            if bridgeweight > maxweight:
                maxweight = bridgeweight
    return maxweight


with open('inputs/24in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')
#print tests

print solve1(tests)
print solve2(tests)
