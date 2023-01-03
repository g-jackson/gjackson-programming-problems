def a(inputs):
    start_stacks = inputs.split('\n\n')[0].split('\n')[:-1][::-1]
    num_stacks = len(inputs.split('\n\n')[0].split('\n')[-1].split('   '))
    instructions = inputs.split('\n\n')[1].split('\n')

    stacks = [[] for x in range(num_stacks)]
    for idx, i in enumerate(start_stacks):
        for j in range(num_stacks):
            char = i[(j * 4) + 1]
            if char != ' ':
                stacks[j].append(char)
            # print(i, j, char, stacks)
    # print(stacks)

    for instruction in instructions:
        move = int(instruction.split(' ')[1])
        from_stack = int(instruction.split(' ')[3]) - 1
        to_stack = int(instruction.split(' ')[5]) - 1
        # print(instruction)
        for i in range(move):
            char = stacks[from_stack].pop()
            stacks[to_stack].append(char)
        # print(stacks)

    result = ''.join([x[-1] for x in stacks])
    return result


def b(inputs):
    start_stacks = inputs.split('\n\n')[0].split('\n')[:-1][::-1]
    num_stacks = len(inputs.split('\n\n')[0].split('\n')[-1].split('   '))
    instructions = inputs.split('\n\n')[1].split('\n')

    stacks = [[] for x in range(num_stacks)]
    for idx, i in enumerate(start_stacks):
        for j in range(num_stacks):
            char = i[(j * 4) + 1]
            if char != ' ':
                stacks[j].append(char)
            # print(i, j, char, stacks)
    # print(stacks)

    for instruction in instructions:
        move = int(instruction.split(' ')[1])
        from_stack = int(instruction.split(' ')[3]) - 1
        to_stack = int(instruction.split(' ')[5]) - 1
        # print(instruction)
        chars = stacks[from_stack][-move:]
        # print(chars, from_stack, to_stack)

        stacks[from_stack] = stacks[from_stack][:-move]
        stacks[to_stack].extend(chars)
        # print(stacks)

    result = ''.join([x[-1] for x in stacks])
    return result


input_file = 'inputs/05test.txt'
input_file = 'inputs/05in.txt'

with open(input_file, 'r') as infile:
    inputs = infile.read()


print(a(inputs))
print(b(inputs))
