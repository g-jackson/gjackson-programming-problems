import hashlib

sample1='''ulqzkmiv'''

def opendoors(hash):
    hashed = hashlib.md5(hash).hexdigest()
    #print hashed
    result = []
    for i in range(4):
        if hashed[i] != "a" and hashed[i].isalpha():
            result.append(True)
        else:
            result.append(False)
    return result


def solve1(intext):
    result = ""
    done = False
    bfs = [((0,0), intext)]
    while not done and len(bfs) != 0:
        sofar = bfs.pop(0)
        pos = sofar[0]
        tohash = sofar[1]
        opened = opendoors(tohash)
        if opened[0]:
            if pos[1] > 0:
                if (pos[0],pos[1]-1) == (3,3):
                    done = True
                    result = tohash+'U'
                bfs.append(((pos[0],pos[1]-1),tohash+'U'))
        if opened[1]:
            if pos[1] < 3:
                if (pos[0],pos[1]+1) == (3,3):
                    done = True
                    result = tohash+'D'
                bfs.append(((pos[0],pos[1]+1),tohash+'D'))
        if opened[2]:
            if pos[0] > 0:
                if (pos[0]-1,pos[1]) == (3,3):
                    done = True
                    result = tohash+'L'                
                bfs.append(((pos[0]-1,pos[1]),tohash+'L'))
        if opened[3]:
            if pos[0] < 3:
                if (pos[0]+1,pos[1]) == (3,3):
                    done = True
                    result = tohash+'R'
                bfs.append(((pos[0]+1,pos[1]),tohash+'R'))

    return result[len(intext):]

def solve2(intext):
    result = 0
    bfs = [((0,0), intext)]
    while len(bfs) != 0:
        #print bfs
        sofar = bfs.pop(0)
        pos = sofar[0]
        tohash = sofar[1]
        opened = opendoors(tohash)
        if opened[0]:
            if pos[1] > 0:
                if (pos[0],pos[1]-1) != (3,3):
                    bfs.append(((pos[0],pos[1]-1),tohash+'U'))
                else:
                    if len(tohash) > result:
                        result = len(tohash)
                        #print tohash                    
        if opened[1]:
            if pos[1] < 3:
                if (pos[0],pos[1]+1) != (3,3):
                    bfs.append(((pos[0],pos[1]+1),tohash+'D'))
                else:
                    if len(tohash) > result:
                        result = len(tohash)
                        #print tohash    
        if opened[2]:
            if pos[0] > 0:
                if (pos[0]-1,pos[1]) != (3,3):
                    bfs.append(((pos[0]-1,pos[1]),tohash+'L'))
                else:
                    if len(tohash) > result:
                        result = len(tohash)
                        #print tohash    
        if opened[3]:
            if pos[0] < 3:
                if (pos[0]+1,pos[1]) != (3,3):
                    bfs.append(((pos[0]+1,pos[1]),tohash+'R'))
                else:
                    if len(tohash) > result:
                        result = len(tohash)
                        #print tohash    
    return result - len(intext) + 1


with open('inputs/17in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests

print solve1(tests)
print solve2(tests)
