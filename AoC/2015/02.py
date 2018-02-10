sample1='''2x3x4
1x1x10'''

def surface(l,w,h):
    return 2*l*w + 2*w*h + 2*h*l

def smallest(l,w,h):
    dim = [l,w,h]
    dim.remove(max(l,w,h))
    return dim[0]*dim[1]

def smallestperimiter(l,w,h):
    dim = [l,w,h]
    dim.remove(max(l,w,h))
    return dim[0]*2 + dim[1]*2

def solve1(intext):
    counter = 0
    for i in intext:
        string = i.split('x')
        l = (int)(string[0])
        w = (int)(string[1])
        h = (int)(string[2])
        counter += surface(l,w,h) + smallest(l,w,h)
        #print surface(l,w,h) + smallest(l,w,h), surface(l,w,h) , smallest(l,w,h)
    return counter

def solve2(intext):
    counter = 0
    for i in intext:
        string = i.split('x')
        l = (int)(string[0])
        w = (int)(string[1])
        h = (int)(string[2])
        counter += (l*w*h) + smallestperimiter(l,w,h)
        #print l*w*h + smallestperimiter(l,w,h), l*w*h , smallestperimiter(l,w,h)
    return counter


with open('inputs/02in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
print solve1(tests)
print solve2(tests)
