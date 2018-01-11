sample1 ='''..#
#..
...'''

import numpy as np
import matplotlib.pyplot as plt

def readinput(inlist,state):
    grid = {}
    for row in range(len(inlist)):
        for column in range(len(inlist)):
            if inlist[row][column] == '#':
                grid[(column,len(inlist)-1-row)] = state
    return grid

def rotateleft(dir):
    dirs = [(0,1), (-1,0) ,(0,-1), (1,0)]
    current = dirs.index(dir)
    if current == 3:
        newdir = dirs[0]
    else:
        newdir = dirs[current+1]
    return newdir

def rotateright(dir):
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    current = dirs.index(dir)
    if current == 3:
        newdir = dirs[0]
    else:
        newdir = dirs[current+1]
    return newdir

def move(grid, viruspos, virusdir):
    currentinfected = False
    if viruspos in grid:
        currentinfected = True
    if currentinfected:
        virusdir = rotateright(virusdir)
        del grid[viruspos]
        viruspos = (viruspos[0]+virusdir[0], viruspos[1]+virusdir[1])
    else:
        virusdir = rotateleft(virusdir)
        grid[viruspos] = 1
        viruspos = (viruspos[0]+virusdir[0], viruspos[1]+virusdir[1])


    return not currentinfected, viruspos, virusdir

def printgrid(grid,pos):
    list(grid.keys())
    minx = -5
    maxx = 5
    miny = -5
    maxy = 5
    for i in grid:
        if i[0] < minx:
            minx = i[0]
        if i[0] > maxx:
            maxx = i[0]
        if i[1] < miny:
            miny = i[1]
        if i[1] > maxy:
            maxy = i[1]
    #print minx, maxx, miny, maxy
    print pos
    for y in range(maxy, miny+1, -1):
        row = '%s\t'%y
        for x in range(minx, maxx+1):
            if (x,y) in grid:
                if (x,y) == pos:
                    row = row + '*'
                else:
                    row = row + '#'
            else:
                if (x,y) == pos:
                    row = row + ','
                else:
                    row = row + '.'
        print row
    print "\n"

def printgrid2(grid):
    thisgrid = list(grid.keys())
    coords = zip(*thisgrid)
    plt.scatter(coords[0], coords[1])
    plt.show()

def solve1(inlist):
    infected = readinput(inlist,1)
    halfgrid = len(inlist)/2
    viruspos = (halfgrid,halfgrid)
    virusdir = (0,1)
    moves = 10000
    infections = 0
    for i in range(moves):
        #print infected
        #print "pos", viruspos, "dir", virusdir
        #printgrid(infected, viruspos)
        infection, viruspos, virusdir = move(infected, viruspos, virusdir)
        infections = infections + infection
    print infected
    #printgrid2(infected)
    
    return infections

def move2(grid, viruspos, virusdir):
    infected = 0
    state = 0
    if viruspos in grid:
        state = grid[viruspos]
    # Clean -> Weakened
    if state == 0:
        virusdir = rotateleft(virusdir)
        grid[viruspos] = 1
        viruspos = (viruspos[0]+virusdir[0], viruspos[1]+virusdir[1])
    # Weakened  -> Infected
    elif state == 1:
        infected = 1
        grid[viruspos] = 2
        viruspos = (viruspos[0]+virusdir[0], viruspos[1]+virusdir[1])
    # Infected -> Flagged
    elif state == 2:
        virusdir = rotateright(virusdir)
        grid[viruspos] = 3
        viruspos = (viruspos[0]+virusdir[0], viruspos[1]+virusdir[1])
    # Flagged -> Cleaned
    elif state == 3:
        virusdir = (virusdir[0]*-1,virusdir[1]*-1)
        del grid[viruspos]
        viruspos = (viruspos[0]+virusdir[0], viruspos[1]+virusdir[1])
    return infected, viruspos, virusdir


def solve2(inlist):
    infected = readinput(inlist,2)
    halfgrid = len(inlist)/2
    viruspos = (halfgrid,halfgrid)
    virusdir = (0,1)
    moves = 10000000
    infections = 0
    for i in range(moves):
        #print infected
        #print "pos", viruspos, "dir", virusdir
        #printgrid(infected, viruspos)
        infection, viruspos, virusdir = move2(infected, viruspos, virusdir)
        infections = infections + infection
    #print infected
    #printgrid2(infected)
    
    return infections
    return


with open('inputs/22in.txt', 'r') as infile:
    test = infile.read()
#test = sample1
#print test

test = test.split('\n')
#print solve1(test)
print solve2(test)

