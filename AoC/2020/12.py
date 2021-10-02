test_inputs = '''F10
N3
F7
R90
F11'''


def a(inputs):
    pos_x = 0
    pos_y = 0
    heading = 0
    for line in inputs:
        instruction = line[0]
        amount = int(line[1:])
        if instruction == 'F':
            if heading == 0:
                instruction = 'E'
            if heading == 90:
                instruction = 'N'
            if heading == 180:
                instruction = 'W'
            if heading == 270:
                instruction = 'S'
        if instruction == 'E':
            pos_x += amount
        if instruction == 'W':
            pos_x -= amount
        if instruction == 'N':
            pos_y += amount
        if instruction == 'S':
            pos_y -= amount
        if instruction == 'L':
            heading = (heading + amount) % 360
        if instruction == 'R':
            heading = (heading - amount) % 360
        print(line, '->', pos_x, pos_y, heading)

    return abs(pos_x) + abs(pos_y)


def b(inputs):
    return


with open('inputs/12in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
