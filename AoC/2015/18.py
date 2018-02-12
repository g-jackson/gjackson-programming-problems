sample1=''''''

def printlights(board):
    maxx = 0
    maxy = 0
    for i in board:
        if maxx < i[0]:
            maxx = i[0]
        if maxy < i[1]:
            maxy = i[1]        

    for y in range(maxy+1):
        for x in range(maxx+1):
            if (x,y) in board:
                print '#',
            else:
                print '.',
        print ""

def readinput(intext):
    lights = []
    for y in range(len(intext)):
        for x in range(len(intext[y])):
            if intext[y][x] == '#':
                lights.append((x,y))
    return lights

def solve1(intext):
    lights = readinput(intext)
    #print lights
    printlights(lights)
    return 

def solve2(intext):

    return 


with open('inputs/18in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')

print solve1(tests)
#print solve2(tests)
