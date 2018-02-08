from collections import deque
from itertools import *

sample1='''swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d'''

def solve1(intext, password):
    password = password
    for line in intext:
        #print ''.join(list(password))
        #print line
        split = line.split()
        if split[0] == "swap" and split[1] == "position":
            x = (int)(split[2])
            y = (int)(split[5])
            temp = password[x]
            password[x] = password[y]
            password[y] = temp

        if split[0] == "swap" and split[1] == "letter":
            x = split[2]
            y = split[5]
            pos1 = password.index(x)
            pos2 = password.index(y)
            password[pos1] = y
            password[pos2] = x
        if split[0] == "rotate" and split[1] == "left":
            x = (int)(split[2])
            password[:] =  password[x:] + password[:x]

        if split[0] == "rotate" and split[1] == "right":
            x = (int)(split[2])
            password[:] =  password[-x:] + password[:-x]

        if split[0] == "rotate" and split[1] == "based":
            x = split[6]
            rotations = password.index(x)
            if rotations > 3:
                rotations = rotations + 2
            else:
                rotations = rotations + 1
            rotations = rotations % len(password)
            password[:] =  password[-rotations:] + password[:-rotations]

        if split[0] == "reverse":
            x = (int)(split[2])
            y = (int)(split[4])
            password = password[0:x] + password[x:y+1][::-1] + password[y+1:]

        if split[0] == "move":
            x = (int)(split[2])
            y = (int)(split[5])
            temp = password[x]
            del password[x]
            password.insert(y,temp)

    return ''.join(list(password))

def solve2(intext):
    result = ""
    for permutation in permutations(list("abcdefgh")):
        password = list(permutation)
        crackedpassword = solve1(intext, password)
        #print ''.join(password), crackedpassword
        if crackedpassword == "fbgdceah":
            result = ''.join(permutation)
            break
    return result


with open('inputs/21in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
print solve1(tests, list("abcdefgh"))
print solve2(tests)
