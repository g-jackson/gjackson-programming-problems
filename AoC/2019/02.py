testinputs = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
#testinputs = [1, 0, 0, 0, 99]
#testinputs = [2, 3, 0, 3, 99]
#testinputs = [2, 4, 4, 5, 99, 0]
#testinputs = [1, 1, 1, 4, 99, 5, 6, 0, 99]

def a(inputs, i, j):
    program = inputs
    #print(program)

    program[1] = i
    program[2] = j

    program_counter = 0
    halt = False
    while not halt:
        pos1 = program[program_counter]
        if pos1 == 99:
            halt = True
        else:
            pos2 = program[program_counter + 1]
            pos3 = program[program_counter + 2]
            pos4 = program[program_counter + 3]
            if pos1 == 1:
                program[pos4] = program[pos2] + program[pos3]
            if pos1 == 2:
                program[pos4] = program[pos2] * program[pos3]
            program_counter += 4
        #print(pos1, pos2, pos3, pos4, program)
    return program[0]


def b(inputs):
    for i in range(100):
        for j in range(100):
            try:
                program = inputs.copy()
                out = a(program, i, j) 
                if out == 19690720:
                    #print(i, j)
                    return 100 * i + j
            except:
                continue
    return out 


with open('inputs/02in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split(",")
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

print(a(inputs.copy(), 12, 2))
print(b(inputs.copy()))
#print tests
