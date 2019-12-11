def a(program, input_value):
    program = program.copy()
    #print(program)
    program_counter = 0
    halt = False
    while not halt:
        #print(program_counter, program)
        pos1 = program[program_counter]
        mode1 =  (pos1 // 100) % 10
        mode2 =  (pos1 // 1000) % 10
        #mode3 =  (pos1 // 10000) % 10
        op_code = pos1 % 100
        if op_code == 99:
            halt = True
            print("halt")
        else:
            if op_code not in [1,2,3,4,5,6,7,8,99]:
                halt = True
                print("invalid opcode:", op_code)

            operand1, operand2, register = "-", "-","-"
            
            # 1 parameter
            if op_code in [3, 4]:
                register = program[program_counter + 1]
                if mode1 == 0 and op_code != 3:
                    register = program[register]
            
            # 2 parameters
            if op_code in [5, 6]:
                parameter1 = program[program_counter + 1]
                register = program[program_counter + 2]
                if mode1 == 0:
                    operand1 = program[parameter1]
                else:
                    operand1 = parameter1
                if mode2 == 0:
                    register = program[register]

            # 3 parameters
            if op_code in [1, 2, 7, 8]:
                parameter1 = program[program_counter + 1]
                parameter2 = program[program_counter + 2]
                register = program[program_counter + 3]
                if mode1 == 0:
                    operand1 = program[parameter1]
                else:
                    operand1 = parameter1
                if mode2 == 0:
                    operand2 = program[parameter2]
                else:
                    operand2 = parameter2
            code_names = ["NULL","ADD", "MUL", "READ", "WRITE", "JNZ", "JEZ", "LESS", "EQ"]
            #print(code_names[op_code], mode1, mode2, register, operand1, operand2)

            # ADD 1 + 2 store in 3
            if op_code == 1:
                program[register] = operand1 + operand2
                program_counter += 4

            # MUL 1 + 2 store in 3
            elif op_code == 2:
                program[register] = operand1 * operand2
                program_counter += 4

            # IN store in 1
            elif op_code == 3:
                #print("Read")
                program[register] = input_value
                program_counter += 2

            # OUT from 1
            elif op_code == 4:
                print("output:", register)
                program_counter += 2

            # Jump to 2 if 1 is non-zero
            elif op_code == 5:
                if operand1 != 0:
                    program_counter = register
                else:
                    program_counter += 3

            # Jump to 2 if 1 is zero
            elif op_code == 6:
                if operand1 == 0:
                    program_counter = register
                else:
                    program_counter += 3

            # Store 1/0 in 3 if 1 less than 2
            elif op_code == 7:
                if operand1 < operand2:
                    program[register] = 1
                else:
                    program[register] = 0
                program_counter +=4

            # Store 1/0 in 3 if 1 equal to 2
            elif op_code == 8:
                if operand1 == operand2:
                    program[register] = 1
                else:
                    program[register] = 0
                program_counter +=4

    #return program[0]


def b(inputs):
    return


with open('inputs/05in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split(",")
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])



testinputs = [1002,4,3,4,33]
testinputs = [1101,100,-1,4,0]
testinputs = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
testinputs = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
testinputs = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


#print(a(inputs, 1))
print(a(inputs, 5))
#print tests