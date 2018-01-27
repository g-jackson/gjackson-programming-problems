sample1='''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''

def solve1(intext):
    registers = {'a':0,'b':0,'c':1,'d':0}
    pc = 0
    while pc < len(intext):
        line = intext[pc]
        line = line.split()
        #print registers
        #print line
        instruction = line[0]
        if instruction == "inc":
            registers[line[1]] = registers[line[1]] + 1
        if instruction == "dec":
            registers[line[1]] = registers[line[1]] - 1
        if instruction == "cpy":
            if line[1].islower():
                registers[line[2]] = registers[line[1]]
            else:
                registers[line[2]] = (int)(line[1])
        if instruction == "jnz":
            if line[1].islower():
                if registers[line[1]] != 0:
                    pc = pc + (int)(line[2])
                else:
                    pc = pc + 1  
            else:
                if (int)(line[1]) != 0:
                    pc = pc + (int)(line[2])
                else:
                    pc = pc + 1  
        else:
            pc = pc + 1    

    print registers
    return registers['a']

def solve2(intext):

    return 


with open('inputs/12in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
print solve1(tests)
#print solve2(tests)
