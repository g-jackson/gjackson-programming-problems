sample1 ='''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''


def solve1(inlist):
    print inlist
    registers = {}
    for instruction in inlist:
        # Split instruction into parts
        instruction = instruction.split(' ')
        reg = instruction[0]
        operator = instruction[1]
        operand = (int)(instruction[2])
        condreg = instruction[4]
        condoperator = instruction[5]
        condoperand = (int)(instruction[6])
        # Add registers if new
        if reg not in registers:
            registers[reg] = 0
        if condreg not in registers:
            registers[condreg] = 0
        print reg, operator, operand, 'if', condreg, condoperator, condoperand
        print registers
        if condoperator == '<':
            if registers[condreg] < condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '>':
            if registers[condreg] > condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                    print 'inc'
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '<=':
            if registers[condreg] <= condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '>=':
            if registers[condreg] >= condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '==':
            if registers[condreg] == condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '!=':
            if registers[condreg] != condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        else:
            print "invalid instruction"

    print registers
    highvalue = registers.popitem()[1]
    for key in registers:
        if registers[key] > highvalue:
            highvalue = registers[key]
    return highvalue

def solve2(inlist):
    print inlist
    highvalue = 0
    registers = {}
    for instruction in inlist:
        for key in registers:
            if registers[key] > highvalue:
                highvalue = registers[key]

        # Split instruction into parts
        instruction = instruction.split(' ')
        reg = instruction[0]
        operator = instruction[1]
        operand = (int)(instruction[2])
        condreg = instruction[4]
        condoperator = instruction[5]
        condoperand = (int)(instruction[6])
        # Add registers if new
        if reg not in registers:
            registers[reg] = 0
        if condreg not in registers:
            registers[condreg] = 0
        print reg, operator, operand, 'if', condreg, condoperator, condoperand
        print registers
        if condoperator == '<':
            if registers[condreg] < condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '>':
            if registers[condreg] > condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                    print 'inc'
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '<=':
            if registers[condreg] <= condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '>=':
            if registers[condreg] >= condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '==':
            if registers[condreg] == condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        elif condoperator == '!=':
            if registers[condreg] != condoperand:
                if operator == 'inc':
                    registers[reg] = registers[reg] + (int)(operand)
                else:
                    registers[reg] = registers[reg] - (int)(operand)

        else:
            print "invalid instruction"

    print registers


    return highvalue



with open('inputs/8in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')

#print test
#print solve1(test)
print solve2(test)

