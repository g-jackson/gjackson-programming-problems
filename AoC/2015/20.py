from math import sqrt
sample1=''''''

def factors(n):
    return list(sorted(set([f(x) for x in range(1, int(n**0.5) + 1) if not n % x 
                for f in (lambda x: x, lambda x: n // x)])))

def solve1(intext):
    i = 1
    while True:
        facs =  factors(i)
        if sum([x*10 for x in facs]) > 29000000:
            return i
        i += 1

# probably more efficient way by reverse engineering the i using increasing factors

def solve2(intext):
    i = 1
    delivered = {}
    while True:
        facs =  factors(i)
        total = 0
        for x in facs:
            if x not in delivered:
                delivered[x] = 0
            
            if delivered[x] != 51:
                total += x*11
                delivered[x] += 1
        if total > 29000000:
            return i
        i += 1

with open('inputs/20in.txt', 'r') as infile:
    tests = infile.read()

tests = sample1
print tests

#print solve1(tests)
print solve2(tests)
