sample1='''10'''

def iswall(intext, coord):
    x = coord[0]
    y = coord[1]
    total = (x*x + 3*x + 2*x*y + y + y*y) + intext
    if bin(total).count('1')%2 == 0:
        return False
    else:
        return True

def printmap(visited, walls):
    maxx = 0
    maxy = 0
    for i in walls:
        if maxx < i[0]:
            maxx = i[0]
        if maxy < i[1]:
            maxy = i[1]        

    for y in range(maxy+1):
        for x in range(maxx+1):
            if (x,y) in visited:
                print ' ',
            elif (x,y) in walls:
                print '#',
            else:
                print '.',
        print ""

def solve1(intext):
    intext = (int)(intext)
    start = (1,1)
    #destination = (7,4)
    destination = (31,39)
    dfs = [(start,1)]
    visited = [(1,1)]
    walls = []
    done = False
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    result = 0
    while not done and len(dfs) > 0:
        sofar = dfs.pop(0)
        #print "processing", sofar
        pos = sofar[0]
        steps = sofar[1]
        for direction in directions:
            newpos = (pos[0]+direction[0],pos[1]+direction[1])
            if newpos[0] >= 0 and newpos[1] >= 0 and newpos not in visited:
                if not iswall(intext, newpos):
                    if newpos == destination:
                        done = True
                        result = steps
                    else:
                        #print "adding to dfs", (newpos,steps+1)
                        visited.append(newpos)
                        dfs.append((newpos,steps+1))
                else:
                    walls.append(newpos)
    #print visited
    printmap(visited, walls)
    return result

def solve2(intext):
    intext = (int)(intext)
    start = (1,1)
    dfs = [(start,1)]
    visited = [(1,1)]
    walls = []
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while len(dfs) > 0:
        sofar = dfs.pop(0)
        #print "processing", sofar
        pos = sofar[0]
        steps = sofar[1]
        for direction in directions:
            newpos = (pos[0]+direction[0],pos[1]+direction[1])
            if newpos[0] >= 0 and newpos[1] >= 0 and newpos not in visited:
                if not iswall(intext, newpos):
                    #print "adding to dfs", (newpos,steps+1)
                    if steps != 51:
                        visited.append(newpos)
                        dfs.append((newpos,steps+1))
                else:
                    walls.append(newpos)
    #print visited
    printmap(visited, walls)
    return len(visited)


with open('inputs/13in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests

print solve1(tests)
print solve2(tests)
