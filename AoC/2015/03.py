sample1=''''''
def solve1(intext):
    visited = []
    pos = (0,0)
    for i in intext:
        if i == "<":
            pos = (pos[0]-1,pos[1])
        if i == ">":
            pos = (pos[0]+1,pos[1])
        if i == "^":
            pos = (pos[0],pos[1]+1)
        if i == "v":
            pos = (pos[0],pos[1]-1)            
        if pos not in visited:
            visited.append(pos)
    return len(visited)

def solve2(intext):
    visited = []
    multipos = [(0,0), (0,0)]
    step = 0
    for i in intext:
        santa = step%2
        pos = multipos[santa]
        if i == "<":
            pos = (pos[0]-1,pos[1])
        if i == ">":
            pos = (pos[0]+1,pos[1])
        if i == "^":
            pos = (pos[0],pos[1]+1)
        if i == "v":
            pos = (pos[0],pos[1]-1)            
        if pos not in visited:
            visited.append(pos)
        multipos[santa] = pos
        step += 1
    return len(visited)


with open('inputs/03in.txt', 'r') as infile:
    tests = infile.read()

test = sample1
#print tests

#print solve1(tests)
print solve2(tests)
