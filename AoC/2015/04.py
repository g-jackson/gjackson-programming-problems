from hashlib import md5
sample1='''abcdef'''
def solve1(intext):
    i = 0
    done = False
    while not done:
        tohash = intext+(str)(i)
        #print tohash
        hashed = md5(tohash).hexdigest()
        hashed = (str)(hashed)
        if hashed[:5] == "00000":
            return i
        i += 1
    return 

def solve2(intext):
    i = 0
    done = False
    while not done:
        tohash = intext+(str)(i)
        #print tohash
        hashed = md5(tohash).hexdigest()
        hashed = (str)(hashed)
        if hashed[:6] == "000000":
            return i
        i += 1
    return 

with open('inputs/04in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests

print solve1(tests)
print solve2(tests)
