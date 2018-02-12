sample1='''inc a
jio a, +2
tpl a
inc a'''


def solve1(intext):
    registers = {'a':0,'b':0}
    pc = 0
    while pc < len(intext) and pc >= 0:
        line = intext[pc].replace(',', '')
        #print registers
        #print pc + 1, ":", line
        split = line.split()
        instruction = split[0]
        reg1 = split[1]
        if instruction == "hlf":
            registers[reg1] /= 2
        if instruction == "tpl":
            registers[reg1] *= 3
        if instruction == "inc":
            registers[reg1] += 1
        if instruction == "jmp":
            jump = (int)(split[1])
            pc += jump - 1
            
        if instruction == "jie":
            jump = (int)(split[2])
            if registers[reg1] % 2 == 0:
                pc += jump - 1

        if instruction == "jio":
            jump = (int)(split[2])
            if registers[reg1] == 1:
                pc += jump - 1
        pc += 1
    #print registers
    return registers['b']

def solve2(intext):
    registers = {'a':1,'b':0}
    pc = 0
    while pc < len(intext) and pc >= 0:
        line = intext[pc].replace(',', '')
        #print registers
        #print pc + 1, ":", line
        split = line.split()
        instruction = split[0]
        reg1 = split[1]
        if instruction == "hlf":
            registers[reg1] /= 2
        if instruction == "tpl":
            registers[reg1] *= 3
        if instruction == "inc":
            registers[reg1] += 1
        if instruction == "jmp":
            jump = (int)(split[1])
            pc += jump - 1
            
        if instruction == "jie":
            jump = (int)(split[2])
            if registers[reg1] % 2 == 0:
                pc += jump - 1

        if instruction == "jio":
            jump = (int)(split[2])
            if registers[reg1] == 1:
                pc += jump - 1
        pc += 1
    #print registers
    return registers['b']


with open('inputs/23in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests

tests = tests.split('\n')
print solve1(tests)
print solve2(tests)
