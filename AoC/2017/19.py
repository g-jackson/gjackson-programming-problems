import pprint

sample1 ='''     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ '''

def solve1(inlist):
    strings = inlist.split('\n')
    lines = []
    letters = ""
    for line in strings:
        lines.append(list(line))
        print line
    pos = [0, lines[0].index('|')]
    direction = [1,0]
    traversing = True
    while traversing:
        print "start:", pos, "direction:", direction
        pos[0] = pos[0] + direction[0]
        pos[1] = pos[1] + direction[1]
        char = lines[pos[0]][pos[1]]
        print char
        if char == '-' or char == '|':
            continue
        elif char.isalpha():
            letters = letters + char
        elif char == '+':
            if (abs(direction[0]) == 1):
                print "changing from vertical to horizontal"
                if pos[1]+1 != len(lines[0]):
                    if lines[pos[0]][pos[1]+1] == '-' or lines[pos[0]][pos[1]+1].isalpha():
                        direction = [0,1]
                    else:
                        direction = [0,-1]
                else:
                    direction = [0,-1]
            else:
                print "changing from horizontal to vertical"
                if pos[0]+1 != len(lines):
                    print pos[0]+1 , len(lines)
                    if lines[pos[0]+1][pos[1]] == '|' or lines[pos[0]+1][pos[1]].isalpha():
                        direction = [1,0]
                    else:
                        direction = [-1,0]
                else:
                    direction = [-1,0]                
        else:
            traversing = False
    return letters


def solve2(inlist):
    strings = inlist.split('\n')
    lines = []
    counter = 0
    letters = ""
    for line in strings:
        lines.append(list(line))
        print line
    pos = [0, lines[0].index('|')]
    direction = [1,0]
    traversing = True
    while traversing:
        counter = counter + 1
        print "start:", pos, "direction:", direction
        pos[0] = pos[0] + direction[0]
        pos[1] = pos[1] + direction[1]
        char = lines[pos[0]][pos[1]]
        print char
        if char == '-' or char == '|':
            continue
        elif char.isalpha():
            letters = letters + char
        elif char == '+':
            if (abs(direction[0]) == 1):
                print "changing from vertical to horizontal"
                if pos[1]+1 != len(lines[0]):
                    if lines[pos[0]][pos[1]+1] == '-' or lines[pos[0]][pos[1]+1].isalpha():
                        direction = [0,1]
                    else:
                        direction = [0,-1]
                else:
                    direction = [0,-1]
            else:
                print "changing from horizontal to vertical"
                if pos[0]+1 != len(lines):
                    print pos[0]+1 , len(lines)
                    if lines[pos[0]+1][pos[1]] == '|' or lines[pos[0]+1][pos[1]].isalpha():
                        direction = [1,0]
                    else:
                        direction = [-1,0]
                else:
                    direction = [-1,0]                
        else:
            traversing = False
    return counter


with open('inputs/19in.txt', 'r') as infile:
    test = infile.read()

#test = sample1

#print test

#print solve1(test)
print solve2(test)

