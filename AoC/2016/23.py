sample1='''cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a'''

def solve1(intext):
    registers = {'a':7,'b':0,'c':0,'d':0}
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
        
        if instruction == "tgl":
            ininstruction = ""
            if pc + registers[line[1]] >= 0 and pc + registers[line[1]] < len(intext):
                ininstruction = intext[pc + registers[line[1]]]
                outinstruction = ""
                if "inc" in ininstruction:
                    outinstruction = "dec " + "".join(ininstruction.split()[1:])
                if "dec" in ininstruction:
                    outinstruction = "inc " + "".join(ininstruction.split()[1:])
                if "tgl" in ininstruction:
                    outinstruction = "inc " + "".join(ininstruction.split()[1:])
                if "jnz" in ininstruction:
                    outinstruction = "cpy " + " ".join(ininstruction.split()[1:])
                if "cpy" in ininstruction:
                    outinstruction = "jnz " + " ".join(ininstruction.split()[1:])
                #print "toggling", intext[pc + registers[line[1]]], "to", outinstruction
                intext[pc + registers[line[1]]] = outinstruction
        
        if instruction == "jnz":
            if line[1].islower():
                if registers[line[1]] != 0:
                    pc = pc + (int)(line[2])
                else:
                    pc = pc + 1  
            else:
                if (int)(line[1]) != 0:
                    if line[2].islower():
                        pc = pc + registers[line[2]]
                    else:
                        pc = pc + (int)(line[2])
                else:
                    pc = pc + 1
        else:
            pc = pc + 1    

    print registers
    return registers['a']

def solve2(intext):

    return 


with open('inputs/23in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests
tests = tests.split('\n')

print solve1(tests)
#print solve2(tests)
