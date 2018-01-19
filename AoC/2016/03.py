sample1='''5 10 25'''
import numpy as np

def solve1(intext):
    validcounter = 0
    for line in intext:
        ts = line.split()
        t1 = (int)(ts[0])
        t2 = (int)(ts[1])
        t3 = (int)(ts[2])
        valid = True
        if (t1 >= t2+t3) or (t2 >= t1+t3) or (t3 >= t1+t2):
            #print t1,t2,t3
            valid = False
        if valid:
            validcounter = validcounter + 1
    return validcounter

def solve2(intext):
    validcounter = 0
    rows = []
    for line in intext:
        rows.append(line.split())
    rows = np.array(rows).flatten('F')
    #print rows, len(rows)
    for i in range(0,len(rows),3):
        ts = rows[i:i+3]
        #print ts
        t1 = (int)(ts[0])
        t2 = (int)(ts[1])
        t3 = (int)(ts[2])
        valid = True
        if (t1 >= t2+t3) or (t2 >= t1+t3) or (t3 >= t1+t2):
            #print t1,t2,t3
            valid = False
        if valid:
            validcounter = validcounter + 1
    return validcounter
     


with open('inputs/03in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split("\n")
#print tests

#print solve1(tests)
print solve2(tests)
