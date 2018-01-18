sample1='''ULL
RRDDD
LURDL
UUUUD'''


def solve1(intext):
    keypad = [[1,2,3],[4,5,6],[7,8,9]]
    pos = [1,1]
    passcode = ""
    for directions in intext:      
        for direction in directions:
            #print direction
            if direction == 'U':
                if pos[0] != 0:
                    pos[0] = pos[0] - 1
            elif direction == 'D':
                if pos[0] != 2:
                    pos[0] = pos[0] + 1                
            elif direction == 'L':
                if pos[1] != 0:
                    pos[1] = pos[1] - 1
            elif direction == 'R':
                if pos[1] != 2:
                    pos[1] = pos[1] + 1
            #print pos
        passcode = passcode + (str)(keypad[pos[0]][pos[1]])
    return passcode

def solve2(intext):

    return 


with open('inputs/02in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')
#print tests

print solve1(tests)
#print solve2(tests)
