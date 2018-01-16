sample1='''R8, R4, R4, R8'''

def rotate(currentdirection, direction):
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    newdir = 0
    if direction == "L":
        newdir = directions.index(currentdirection) + 1
        if newdir > 3:
            newdir = 0
        newdir = directions[newdir]

    elif direction == "R":
        newdir = directions.index(currentdirection) - 1
        if newdir < 0:
            newdir = 3
        newdir = directions[newdir]
    else:
        print "invalid direction"
    return newdir

def solve1(intext):
    pos = (0,0)
    direction = (0,1)
    print  pos, direction
    for i in intext:
        direction = rotate(direction,i[0])
        pos = (pos[0]+((int)(i[1:])*direction[0]), pos[1]+((int)(i[1:])*direction[1]))
        #print i, pos, direction
    return abs(pos[0]) + abs(pos[1])

def solve2(intext):
    pos = (0,0)
    direction = (0,1)
    #print  pos, direction
    points = []
    result = -1
    for i in intext:
        
        direction = rotate(direction,i[0])
        distance = (int)(i[1:])
        for step in range(distance):
            thisstep = ((pos[0]+step*direction[0]), pos[1]+step*direction[1])
            if result == -1:
                if thisstep in points: 
                    #print points         
                    #print thisstep
                    result =  abs(thisstep[0]) + abs(thisstep[1])
            points.append(thisstep)
        pos = (pos[0]+distance*direction[0]), pos[1]+((int)(i[1:])*direction[1])
        

        #print i, pos, direction
    return result


with open('inputs/01in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split(', ')
#print tests

#print solve1(tests)
print solve2(tests)
