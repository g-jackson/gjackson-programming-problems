import sys
from itertools import permutations
sample1='''###########
#0.1.....2#
#.#######.#
#4.......3#
###########'''

def printmap(walls, values):
    maxx = 0
    maxy = 0
    for i in walls:
        if maxx < i[0]:
            maxx = i[0]
        if maxy < i[1]:
            maxy = i[1]        

    for y in range(maxy+1):
        for x in range(maxx+1):
            if (x,y) in values:
                sys.stdout.write(values[(x,y)])
            elif (x,y) in walls:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')
    sys.stdout.flush()

def readinput(intext):
    locations = {}
    walls = []
    for y in range(len(intext)):
        for x in range(len(intext[y])):
            if intext[y][x] == '#':
                walls.append((x,y))
            if intext[y][x].isdigit():
                locations[(x,y)] = intext[y][x]
    return walls, locations

def shortestpath(tolocation, fromlocation, walls):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    bfs = [(fromlocation,1)]
    visited = [fromlocation]
    #print "processing", sofar

    done = False
    result = 0
    while not done and len(bfs) > 0:
        sofar = bfs.pop(0)
        pos = sofar[0]
        steps = sofar[1]
        #print bfs
        for direction in directions:
            newpos = (pos[0]+direction[0],pos[1]+direction[1])
            if newpos not in walls and newpos not in visited:
                if newpos == tolocation:
                    done = True
                    result = steps
                    break
                else:
                    #print "adding to bfs", (newpos,steps+1)
                    visited.append(newpos)
                    bfs.append((newpos,steps+1))

    return result

def solve1(intext):
    walls, locations = readinput(intext)
    printmap(walls, locations)
    # distancelookup = {'1': {'0': 266, '3': 26, '2': 74, '5': 266, '4': 252, '7': 52, '6': 86}, 
    #                 '0': {'1': 266, '3': 252, '2': 208, '5': 44, '4': 26, '7': 246, '6': 196}, 
    #                 '3': {'1': 26, '0': 252, '2': 72, '5': 252, '4': 238, '7': 38, '6': 72}, 
    #                 '2': {'1': 74, '0': 208, '3': 72, '5': 208, '4':194, '7': 78, '6': 56}, 
    #                 '5': {'1': 266, '0': 44, '3': 252, '2': 208, '4': 26, '7': 246, '6': 196}, 
    #                 '4': {'1': 252, '0': 26, '3': 238, '2': 194, '5': 26, '7': 232, '6': 182}, 
    #                 '7': {'1': 52, '0': 246, '3': 38, '2': 78, '5': 246, '4': 232, '6': 66}, 
    #                 '6': {'1': 86, '0': 196,'3': 72, '2': 56, '5': 196, '4': 182, '7': 66}}
    distancelookup = {}
    for fromlocation in locations:
        distances = {}
        for tolocation in locations:
            if tolocation != fromlocation:
                print "from", locations[fromlocation], fromlocation,"to", locations[tolocation], tolocation
                distances[locations[tolocation]] = shortestpath(fromlocation,tolocation, walls)
        distancelookup[locations[fromlocation]] = distances
    

    for location in distancelookup:
        print location, distancelookup[location]
    start = (0,0)
    for location in locations:
        if locations[location] == '0':
            start = location


    shortest = 10000
    for permutation in permutations(range(1,len(locations))):
        order = list(permutation)
        current = 0
        distance = 0
        for i in order:
            distance += distancelookup[(str)(current)][(str)(i)]
            current = i
        if distance < shortest:
            print order
            shortest = distance
    return shortest

def solve2(intext):
    walls, locations = readinput(intext)
    printmap(walls, locations)
    # distancelookup = {'1': {'0': 266, '3': 26, '2': 74, '5': 266, '4': 252, '7': 52, '6': 86}, 
    #                 '0': {'1': 266, '3': 252, '2': 208, '5': 44, '4': 26, '7': 246, '6': 196}, 
    #                 '3': {'1': 26, '0': 252, '2': 72, '5': 252, '4': 238, '7': 38, '6': 72}, 
    #                 '2': {'1': 74, '0': 208, '3': 72, '5': 208, '4':194, '7': 78, '6': 56}, 
    #                 '5': {'1': 266, '0': 44, '3': 252, '2': 208, '4': 26, '7': 246, '6': 196}, 
    #                 '4': {'1': 252, '0': 26, '3': 238, '2': 194, '5': 26, '7': 232, '6': 182}, 
    #                 '7': {'1': 52, '0': 246, '3': 38, '2': 78, '5': 246, '4': 232, '6': 66}, 
    #                 '6': {'1': 86, '0': 196,'3': 72, '2': 56, '5': 196, '4': 182, '7': 66}}
    distancelookup = {}
    for fromlocation in locations:
        distances = {}
        for tolocation in locations:
            if tolocation != fromlocation:
                distances[locations[tolocation]] = shortestpath(fromlocation,tolocation, walls)
                print "from", locations[fromlocation], fromlocation,"to", locations[tolocation], tolocation, "steps:", distances[locations[tolocation]]
        distancelookup[locations[fromlocation]] = distances
    

    for location in distancelookup:
        print location, distancelookup[location]
    start = (0,0)
    for location in locations:
        if locations[location] == '0':
            start = location


    shortest = 10000
    for permutation in permutations(range(1,len(locations))):
        order = list(permutation)
        order.append(0)
        current = 0
        distance = 0
        for i in order:
            distance += distancelookup[(str)(current)][(str)(i)]
            current = i
        if distance < shortest:
            print order
            shortest = distance
    return shortest


with open('inputs/24in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
#print solve1(tests)
print solve2(tests)
