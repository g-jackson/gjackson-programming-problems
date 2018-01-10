from string import ascii_lowercase  
from itertools import repeat, izip
from collections import OrderedDict
from multiprocessing import Process, Queue, freeze_support
import time

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

sample2 ='''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''

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

def run(inlist, ownqueue, coqueue, prognumber):
    registers = OrderedDict(izip(ascii_lowercase, repeat(0)))
    registers['p'] = prognumber
    pc = 0
    sends = 0
    while (pc >= 0) and (pc < len(inlist)):
        line = inlist[pc]
        print prognumber, line, sends, registers
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
            if line[1].islower():
                value = registers[line[1]]
            else:
                value = (int)(line[1])
            ownqueue.put(value)
            #print "sending", value
            sends = sends + 1
        elif instruction == "set":
            registers[reg] = value
        elif instruction == "add":
            registers[reg] = registers[reg] + value
        elif instruction == "mul":
            registers[reg] = registers[reg] * value
        elif instruction == "mod":
            registers[reg] = registers[reg] % value
        elif instruction == "rcv":
            print prognumber, line, sends, registers
            received = coqueue.get()
            registers[reg] = received
            #print "receiving", received

        if instruction == "jgz":
            if line[1].islower():
                jumpcheck = registers[line[1]]
            else:
                jumpcheck = (int)(line[1])
            if jumpcheck > 0:
                pc = pc + value
            else:
                pc = pc + 1
        else:
            pc = pc + 1

    print sends
    return sends

#Could be tidied up to find end condition instead of printing and reading output
def solve2(inlist):
    if __name__ == "__main__":
        freeze_support()
        q0 = Queue()
        q1 = Queue()
        p0 = Process(target=run, args=(inlist, q0, q1, 0))
        p1 = Process(target=run, args=(inlist, q1, q0, 1))
        p0.start()
        #time.sleep(0.5)
        p1.start()

        p0.join()
        p1.join()
        print p1




with open('inputs/18in.txt', 'r') as infile:
    test = infile.read()

#test = sample2
test = test.split('\n')

#print test
#print solve1(test)
print solve2(test)