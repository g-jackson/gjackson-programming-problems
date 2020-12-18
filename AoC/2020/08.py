import copy


def a(inputs):
    file = []
    for line in inputs:
        file.append(line.split(' '))
    acc, _ = machine(file)
    return acc


def machine(file):
    run = True
    acc = 0
    pc = 0
    visited = []
    while run:
        instruction = file[pc]
        if instruction[0] == 'acc':
            acc += int(instruction[1])
        if instruction[0] == 'jmp':
            pc += int(instruction[1]) - 1
        pc += 1
        if pc not in visited:
            visited.append(pc)
        else:
            run = False
        if pc > len(file) - 1:
            run = False
    # print(acc, pc)
    valid = True if pc == len(file) else False
    return acc, valid


def b(inputs):
    file = []
    acc = 0
    for line in inputs:
        file.append(line.split(' '))
    for line in range(len(file)):
        if file[line][0] != 'acc':
            test_file = copy.deepcopy(file)
            if file[line][0] == 'jmp':
                test_file[line][0] = 'nop'
            elif file[line][0] == 'nop':
                test_file[line][0] = 'jmp'
            # print(line, test_file[line], file[line])
            acc, valid = machine(test_file)
            if valid:
                break
    return acc


with open('inputs/08in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
