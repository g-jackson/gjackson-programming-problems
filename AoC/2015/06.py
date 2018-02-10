from sets import Set
sample1='''turn on 0,0 through 19,19
toggle 0,0 through 20,0
turn off 19,19 through 20,20'''

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

def getlights(x,y):
    lights = Set([])
    for i in range((int)(x[0]),(int)(y[0])+1):
        for j in range((int)(x[1]),(int)(y[1])+1):
            lights.add((i,j))
    return lights

def changelights(board, lights, mode):
    #print mode, lights, board
    if mode == "on":
        board |= lights
    if mode == "off":
        board -= lights
    if mode == "toggle":
        board ^= lights

def solve1(intext):
    board = Set([])
    for line in intext:
        split = line.split()
        x = split[-3].split(',')
        y = split[-1].split(',')
        lights = getlights(x,y)
        mode = ""
        if split[0] == "toggle":
            mode = "toggle"
        elif split[1] == "on":
            mode = "on"
        else:
            mode = "off"
        changelights(board,lights,mode)
        #printlights(board)
    return len(board)

def changebrightness(board, lights, mode):
    #print mode, lights, board
    if mode == "on":
        for light in lights:
            board[light[0]][light[1]] += 1
    if mode == "toggle":
        for light in lights:
            board[light[0]][light[1]] += 2
    if mode == "off":
        for light in lights:
            if board[light[0]][light[1]] != 0:
                board[light[0]][light[1]] -= 1

def solve2(intext):
    board = []
    for i in range(1000):
        board.append([0] * 1000)
    for line in intext:
        split = line.split()
        x = split[-3].split(',')
        y = split[-1].split(',')
        lights = getlights(x,y)
        mode = ""
        if split[0] == "toggle":
            mode = "toggle"
        elif split[1] == "on":
            mode = "on"
        else:
            mode = "off"
        changebrightness(board,lights,mode)
        #printlights(board)

    counter = 0
    for i in board:
        for j in i:
            counter += j
    return counter


with open('inputs/06in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')
#print tests

#print solve1(tests)
print solve2(tests)
