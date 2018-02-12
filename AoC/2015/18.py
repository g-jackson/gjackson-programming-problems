sample1='''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''

def printlights(board,size):
    for y in range(size):
        for x in range(size):
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

def update(lights,size):
    newstate = []
    adjacents = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for y in range(size):
        for x in range(size):
            adjacentsum = 0
            for adjacent in adjacents:
                if (x+adjacent[0],y+adjacent[1]) in lights:
                    adjacentsum += 1
            if (adjacentsum == 2 or adjacentsum == 3) and (x,y) in lights:
                newstate.append((x,y))
            elif adjacentsum == 3:
                newstate.append((x,y))
    return newstate

def solve1(intext):
    size = len(intext[0])
    lights = readinput(intext)
    #print lights
    printlights(lights,size)
    for i in range(100):
        lights = update(lights,size)
        print len(lights)
        #printlights(lights, size)  
    return len(lights)

def updateb(lights,size):
    newstate = []
    adjacents = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for y in range(size):
        for x in range(size):
            adjacentsum = 0
            for adjacent in adjacents:
                if (x+adjacent[0],y+adjacent[1]) in lights:
                    adjacentsum += 1
            if (adjacentsum == 2 or adjacentsum == 3) and (x,y) in lights:
                newstate.append((x,y))
            elif adjacentsum == 3:
                newstate.append((x,y))
            elif (x == size -1 and y == size -1) or (x == size -1 and y == 0) or (x == 0 and y == size -1) or (x == 0 and y == 0):
                newstate.append((x,y))
    return newstate

def solve2(intext):
    size = len(intext[0])
    lights = readinput(intext)
    lights.append((0,0))
    lights.append((0,size-1))
    lights.append((size-1,0))
    lights.append((size-1,size-1))
    #print lights
    printlights(lights,size)
    for i in range(100):
        lights = update(lights,size)
        print len(lights)
        printlights(lights, size)  
    return len(lights)


with open('inputs/18in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')

#print solve1(tests)
print solve2(tests)
