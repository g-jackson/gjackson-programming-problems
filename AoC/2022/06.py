def a(inputs):
    for i in range(len(inputs) - 4):
        window = inputs[i: i+4]
        # print(i, window)
        if len(set(window)) == 4:
            return i + 4


def b(inputs):
    for i in range(len(inputs) - 14):
        window = inputs[i: i+14]
        # print(i, window)
        if len(set(window)) == 14:
            return i + 14


input_file = 'inputs/06test.txt'
input_file = 'inputs/06in.txt'

with open(input_file, 'r') as infile:
    inputs = infile.read()


print(a(inputs))
print(b(inputs))
