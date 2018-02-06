sample1=''''''
def solve1(intext):
    registers = {'a':196,'b':0,'c':0,'d':0}
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

        if instruction == "out":
            print "OUT", registers[line[1]]
        
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

# cpy a d     |           | a = x, b = 362, c = 7, d = x
# cpy 7 c     |           | 
# cpy 362 b   |           | 
# inc d       |           | 
# dec b       |           | 
# jnz b -2    |           | a = x, b = 0, c = 7, d = x + 362
# dec c       |           | 
# jnz c -5    |           | d = x + 7 * 362
# cpy d a     |           | a = x + 2534
# jnz 0 0     |           | 
# cpy a b     |           | 
# cpy 0 a     |           | 
# cpy 2 c     |           | a = 0, x + 2534 , c = 2
# jnz b 2     |           | until b = 0 take 2 from b and one from a (div by 2)
# jnz 1 6     |           | 
# dec b       |           | 
# dec c       |           | 
# jnz c -4    |           | 
# inc a       |           | 
# jnz 1 -7    |           | 
# cpy 2 b     |           | a = (x + 2534)/2 , b = 2, c = (x + 2534)%2+1
# jnz c 2     |           | 
# jnz 1 4     |           | 
# dec b       |           | 
# dec c       |           | 
# jnz 1 -4    |           | if c = 2 b = 1 if c = 1 b = 0
# jnz 0 0     |           | 
# out b       |           | b should alternate 1 and 0 so x+2534 where div 2 should give ...,0,1,0,1,...
# jnz a -19   |           | keep dividing a by 2 until a = 0
# jnz 1 -21   |           | reset a to x+2534 and repeat

# x + 2534 needs lowest value where binary is alternating 0s and 1s including head and tail being opposites
# '0b100111100110' = 2534 in binary
# '0b101010101010' = 2730 is the next value which has alternating binary digits 
# x = 2730 - 2534 = 196


with open('inputs/25in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split("\n")
print tests

print solve1(tests)
#print solve2(tests)
