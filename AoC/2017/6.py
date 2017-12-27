def solve1(registers):
    pastresults = {}
    newstate = True
    steps = 0
    while newstate:
        print "step: ", steps, "registers: ", registers
        reallocate = registers.index(max(registers))
        size = registers[reallocate]
        registers[reallocate] = 0
        pointer = reallocate + 1
        for _ in range(size):
            if pointer >= len(registers):
                pointer = 0
            registers[pointer] += 1
            pointer += 1
        print "new registers", registers
        steps += 1
        saveregs = ', '.join(str(x) for x in registers)
        print saveregs
        if saveregs in pastresults:
            newstate = False
        else: 
            pastresults[saveregs] = True
    
    return steps


def solve2(registers):
        pastresults = {}
        newstate = True
        steps = 0
        firstappearance = 0
        while newstate:
            print "step: ", steps, "registers: ", registers
            reallocate = registers.index(max(registers))
            size = registers[reallocate]
            registers[reallocate] = 0
            pointer = reallocate + 1
            for _ in range(size):
                if pointer >= len(registers):
                    pointer = 0
                registers[pointer] += 1
                pointer += 1
            print "new registers", registers
            steps += 1
            saveregs = ', '.join(str(x) for x in registers)
            print saveregs
            if saveregs in pastresults:
                firstappearance = pastresults[saveregs]
                newstate = False
            else: 
                pastresults[saveregs] = steps
        print "steps: ", steps, "firstappearance: ", firstappearance
        return steps - firstappearance


test = [0,2,7,0]
test2 = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]
print solve2(test)