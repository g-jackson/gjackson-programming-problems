from copy import deepcopy
from sets import Set

def issafe(floors):
    safe = True
    for floor in floors:
        generator = False
        for i in floor:
            if i[1] == 'G':
                generator = True
        if generator:
            for i in floor:
                if i[1] == 'C' and (i[0]+'G' not in floor):
                    safe = False
                    #print "floors", floors, "unsafe floor", floor, i
    return safe
    
def genstate(newfloors,elevatorpos):
    state = []
    for floor in newfloors:
        G = 0
        C = 0
        P = 0
        for i in floor:
            if i[1] == 'G':
                if i[0]+'C' in floor:
                    P += 1
                else:
                    G += 1
            else:
                if i[0]+'G' not in floor:
                    C += 1
        state.append((G,C,P))
    #print newfloors, state
    return ((str)(state),elevatorpos)

def move(floors, elements, direction, elevatorpos, steps, bfs, prevstates, result):
    newfloors = deepcopy(floors)
    for i in elements:
        newfloors[elevatorpos].remove(i)
        newfloors[elevatorpos+direction].add(i)
    state = genstate(newfloors,elevatorpos+direction)
    if issafe(newfloors) and state not in prevstates:
        if len(newfloors[0]) == 0 and len(newfloors[1]) == 0 and len(newfloors[2]) == 0:
            result = steps+1
        prevstates.append(state)
        bfs.append((newfloors,elevatorpos+direction,steps+1))
    return result

def solve1(intext):
    floors = intext
    #print floors
    prevstates = [genstate(floors,0)]
    bfs = [(floors,0,0)]
    result = 0
    maxstep = 0
    while result == 0:# and len(bfs) > 0:
        sofar = bfs.pop(0)
        thisfloor =  sofar[0]
        elevatorpos = sofar[1]
        steps = sofar[2]
        if steps > maxstep:
            print "step:", steps, "states on this step:", len(bfs) + 1, "states seen:", len(prevstates)
            maxstep = steps
        for i in thisfloor[elevatorpos]:
            for j in thisfloor[elevatorpos]:
                if i == j:
                    if elevatorpos > 0:
                        result = move(thisfloor, [i], -1, elevatorpos, steps, bfs, prevstates, result)
                    if elevatorpos < 3:
                        result = move(thisfloor, [i], +1, elevatorpos, steps, bfs, prevstates, result)
                else: 
                    if elevatorpos > 0:
                        result = move(thisfloor, [i,j], -1, elevatorpos, steps, bfs, prevstates, result)
                    if elevatorpos < 3:
                        result = move(thisfloor, [i,j], +1, elevatorpos, steps, bfs, prevstates, result)
    return result

def solve2(intext):

    return 

sample1 = [Set(['HC','LC']),Set(['HG']),Set(['LG']),set([])]
tests = [Set(['TG','TM','PG','SG']),Set(['PM','SM']),Set(['OG','OM','RG','RM']),Set([])]
# Takes 1hour+ could be simpilied by only running one of a matching pair on a level 
#tests = [Set(['EG','EM','DG','DM','TG','TM','PG','SG']),Set(['PM','SM']),Set(['OG','OM','RG','RM']),Set([])]

#tests = sample1

#print tests

print solve1(tests)
#print solve2(tests)
