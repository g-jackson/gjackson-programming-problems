sample1 ='''
'''
import sympy
from collections import OrderedDict

def createregisters():
    registers = OrderedDict()
    registers['a'] = 0
    registers['b'] = 0
    registers['c'] = 0
    registers['d'] = 0
    registers['e'] = 0
    registers['f'] = 0
    registers['g'] = 0
    registers['h'] = 0
    return registers

def solve1(inlist):
    registers = createregisters()
    pc = 0
    muls = 0
    while (pc >= 0) and (pc < len(inlist)):
        line = inlist[pc]
        print registers
        print line
        line = line.split(' ')
        instruction = line[0]
        reg = line[1]

        if line[2].islower():
            value = registers[line[2]]
        else:
            value = (int)(line[2])

        if instruction == "set":
            registers[reg] = value
        elif instruction == "sub":
            registers[reg] = registers[reg] - value
        elif instruction == "mul":
            registers[reg] = registers[reg] * value
            muls = muls + 1
        elif instruction == "jnz":
            if line[1].islower():
                compare = registers[line[1]]
            else:
                compare = (int)(line[1])
            if compare != 0:
                pc = pc + value - 1
        pc = pc + 1
    return muls

def solve2(a,b,c):
    notprimes = []
    numbers = range(a, b+1, c)
    for number in numbers:
        #print number
        if not sympy.isprime(number):
            notprimes.append(number)
    return len(notprimes)


with open('inputs/23in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')


#print test
#print solve1(test)

print solve2(106500, 123500, 17)

