sample1 ='''65
8921'''

def generate(start, factor):
    return (start*factor)%2147483647

def solve1(inlist):
    startA = (int)(inlist[0])
    startB = (int)(inlist[1])
    facA = 16807
    facB = 48271
    matches = 0
    iterations = 40000000
    for i in range(iterations):
        startA = generate(startA, facA)
        startB = generate(startB, facB)
        #print startA, startB
        bits = 1 << 16
        bitsA = bin(startA & (bits - 1))
        bitsB = bin(startB & (bits - 1))
        #print bitsA, bitsB
        if bitsA == bitsB:
            matches = matches+1
    return matches

def solve2(inlist):
    startA = (int)(inlist[0])
    startB = (int)(inlist[1])
    facA = 16807
    facB = 48271
    matches = 0
    iterations = 5000000
    listA = []
    listB = []
    bits = 1 << 16

    while len(listA) < iterations:
        startA = generate(startA, facA)
        if startA % 4 == 0:
            if len(listA) % 1000000 == 0:
                print len(listA)
            listA.append(bin(startA & (bits - 1)))
    print "A complete"
    
    while len(listB) < iterations:
        startB = generate(startB, facB)
        if startB % 8 == 0:
            if len(listB) % 1000000 == 0:
                print len(listB)
            listB.append(bin(startB & (bits - 1)))        
    print "B complete"

    #print listA, listB
    for i in range(iterations):
        if listA[i] == listB[i]:
            matches = matches+1
    return matches


test ='''634
301'''

#test = sample1
test = test.split('\n')

#print test
#print solve1(test)
print solve2(test)

