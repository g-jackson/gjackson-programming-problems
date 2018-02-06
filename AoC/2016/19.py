from collections import deque
import math

sample1='''13'''
def solve1a(intext):
    elfs = (int)(intext)
    presents = []
    for i in range(elfs):
        presents.append(1)
    pointer = 0
    result = 0
    newtotal = 0
    #print presents
    while newtotal != elfs:
        if presents[pointer] != 0:
            stolen = False
            i = 0
            while stolen == False:
                i += 1
                stealing = pointer + i
                if stealing > elfs - 1:
                    stealing = stealing - elfs
                if presents[stealing] != 0 and stolen == False:
                    presents[pointer] += presents[stealing]
                    if presents[pointer] > newtotal:
                        newtotal = presents[pointer]
                        #print newtotal
                    result = pointer
                    presents[stealing] = 0
                    stolen = True
                    #print "pointer", pointer, "stealing", stealing, presents
        if pointer == elfs - 1:
            pointer = 0
        else:
            pointer += 1
    return result + 1

def solve2a(intext):
    startelfs = (int)(intext)
    circle = []
    for i in range(startelfs):
        circle.append(i+1)
    done = False
    position = 0
    while not done:
        stealingpos = ((len(circle)/2) + position) % len(circle)
        #print  circle, "pos, stealpos", position, stealingpos#, circle[position], circle[stealingpos]
        del circle[stealingpos]
        if position <= len(circle)-1:
            if stealingpos > position:
                position = position + 1
        else:
            position = 0           
        if len(circle) == 1:
            done = True
        if len(circle) % 10000 == 0:
            print len(circle)
    return circle[0]

def solve2b(intext):
    startelfs = (int)(intext)
    result = 0
    n = 1
    while n * 3 < startelfs:
        n = n * 3
    if n == startelfs:
        result = n
    else:
        result = startelfs - n + max(n-2*startelfs,0)
    return result

def solve2c(intext):
    n = (int)(intext)
    p = 3**int(math.log(n-1,3))
    return n-p+max(n-2*p,0)

with open('inputs/19in.txt', 'r') as infile:
    tests = infile.read()


#tests = sample1
#print tests

#print solve1a(tests)
print solve2c(tests)
print solve2a(tests)
#print solve2b(tests)
