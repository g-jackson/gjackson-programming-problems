test_inputs1 = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''


def a(inputs):
    horizontal = 0
    vertical = 0
    for line in inputs:
        dir = line.split()[0]
        val = int(line.split()[1])
        # print(dir, val)
        if dir == 'up':
            vertical += val
        if dir == 'down':
            vertical -= val
        if dir == 'forward':
            horizontal += val
    return abs(horizontal * vertical)


def b(inputs):
    horizontal = 0
    vertical = 0
    aim = 0
    for line in inputs:
        dir = line.split()[0]
        val = int(line.split()[1])
        # print(dir, val)
        if dir == 'up':
            aim -= val
        if dir == 'down':
            aim += val
        if dir == 'forward':
            horizontal += val
            vertical += (val * aim)
    return abs(horizontal * vertical)


with open('inputs/02in.txt', 'r') as infile:
    inputs = infile.read()
# inputs = test_inputs1
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
