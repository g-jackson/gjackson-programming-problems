from string import ascii_lowercase  
from itertools import repeat, izip
from collections import OrderedDict

sample1 ='''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''

def solve1(inlist):
    registers = OrderedDict(izip(ascii_lowercase, repeat(0)))
    notes = []
    pc = 0
    recovered = 0
    while (pc >= 0) and (pc < len(inlist)) and (recovered == 0):
        line = inlist[pc]
        print registers
        print line
        line = line.split(' ')
        instruction = line[0]
        reg = line[1]
        value = 0
        if len(line) == 3:
            if line[2].islower():
                value = registers[line[2]]
            else:
                value = (int)(line[2])
        if instruction == "snd":
            notes.append(registers[reg])
        elif instruction == "set":
            registers[reg] = value
        elif instruction == "add":
            registers[reg] = registers[reg] + value
        elif instruction == "mul":
            registers[reg] = registers[reg] * value
        elif instruction == "mod":
            registers[reg] = registers[reg] % value
        elif instruction == "rcv":
            if line[-1] != 0:
                recovered = line[-1]

        if instruction == "jgz":
            if registers[reg] > 0:
                pc = pc + value
            else:
                pc = pc + 1
        else:
            pc = pc + 1
    return notes[-1]

def solve2(inlist):

    return inlist


with open('18in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')

#print test
print solve1(test)
#print solve2(test)