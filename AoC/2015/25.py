sample1=''''''

def getpos(row,col):
    diagonal = sum(range(row+col-1))+1
    pos = diagonal + col -1
    return pos

def getvalue(iteration):
    i = 20151125
    for _ in range(1, iteration):
        i *= 252533
        i %= 33554393
    return i

def solve1(intext):
    row = (int)(intext.split()[-3][:-1])
    col = (int)(intext.split()[-1][:-1])
    print row,col
    pos = getpos(row,col)
    print pos
    return getvalue(pos)

def solve2(intext):

    return 

with open('inputs/25in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests

print solve1(tests)
#print solve2(tests)
