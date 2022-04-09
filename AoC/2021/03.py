test_inputs1 = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''


def a(inputs):
    input_length = len(inputs[0])
    frequency = [0] * input_length
    for i in inputs:
        for pos, bit in enumerate(i):
            if int(bit):
                frequency[pos] += 1

    gamma = ''
    epsilon = ''
    for i in frequency:
        if i > len(inputs) / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    return int(gamma, 2) * int(epsilon, 2)


def gas_reading(inputs, keep_val):
    remaining_inputs = inputs.copy()
    pos = 0
    while len(remaining_inputs) > 1:
        score = 0
        for i in remaining_inputs:
            if int(i[pos]):
                score += 1
        if (score >= len(remaining_inputs) / 2) == keep_val:
            keep = '1'
        else:
            keep = '0'
        remove_list = []
        for i in remaining_inputs:
            if i[pos] != keep:
                remove_list.append(i)
        for i in remove_list:
            remaining_inputs.remove(i)
        pos += 1
    return int(remaining_inputs[0], 2)


def b(inputs):
    return gas_reading(inputs, True) * gas_reading(inputs, False)


with open('inputs/03in.txt', 'r') as infile:
    inputs = infile.read()
# inputs = test_inputs1
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
