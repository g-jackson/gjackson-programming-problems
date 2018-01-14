sample1 ='''0: 3
1: 2
4: 4
6: 4'''

def inputranges(inlist):
    ranges = []
    lastgate = (int)(inlist[-1].split(':')[0])
    for i in range(lastgate+1):
        ranges.append(0)
    for i in inlist:
        column = (int)(i.split(':')[1])-1
        crange = (int)(i.split(':')[0])
        ranges[crange] = column
    return ranges

def inputranges2(inlist):
    ranges = []
    lastgate = (int)(inlist[-1].split(':')[0])
    for i in range(lastgate+1):
        ranges.append(0)
    for i in inlist:
        column = (int)(i.split(':')[1])
        crange = (int)(i.split(':')[0])
        ranges[crange] = column
    return ranges

def update(pos, ranges, direction):
    for i in range(len(pos)):
        if ranges[i] != 0:
            if pos[i] == ranges[i]:
                direction[i] = direction[i]*(-1)
                pos[i] = pos[i] + direction[i]
            elif pos[i] == 0:
                direction[i] = direction[i]*(-1)
                pos[i] = pos[i] + direction[i]
            else:
                pos[i] = pos[i] + direction[i]
    return pos

def solve1(inlist, startpos):
    ranges = inputranges(inlist)
    #print ranges
    pos = []
    direction = []
    for i in range(len(ranges)):
        if ranges[i] != 0:
            pos.append(0)
        else:
            pos.append(-1)
        direction.append(-1)
    #print pos
    severity = 0
    for i in range(startpos):
        pos = update(pos, ranges, direction)
    #print pos
    for i in range(len(ranges)):
        if pos[i] == 0:
            severity = severity + (i*(ranges[i]+1))
        pos = update(pos, ranges, direction)
        print pos
    return severity

def solve2a(inlist):
    pico = 0
    solved = False
    while not solved:
        
        if solve1(inlist, pico) == 0:
            solved = True
        else:
            print pico, "failed"
            pico = pico + 1


def runpico(pico, ranges):
    #print "running", pico
    success = True
    gate = 0
    for current in range(pico,len(ranges)+pico):
        if ranges[gate] != 0:
            #print "gate has ranges", ranges[gate], "pico", current, "mod result", current % ((ranges[gate]*2) -2)
            if current % ((ranges[gate]*2) -2) == 0:
                success = False
        gate = gate + 1
    return success

#improved solution
def solve2b(inlist):
    ranges = inputranges2(inlist)
    print ranges
    solved = False
    pico = 0
    while not solved:
        pico = pico + 1
        solved = runpico(pico,ranges)
    return pico


with open('inputs/13in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')

#print test
#print solve1(test,0)
print solve2b(test)

