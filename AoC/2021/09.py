test_inputs = '''2199943210
3987894921
9856789892
8767896789
9899965678'''


def a(inputs):
    total_risk = 0
    for r in range(len(inputs)):
        for c in range(len(inputs[r])):
            up = down = left = right = 10
            if r != 0:
                up = int(inputs[r - 1][c])
            if r != len(inputs) - 1:
                down = int(inputs[r + 1][c])
            if c != 0:
                left = int(inputs[r][c - 1])
            if c != len(inputs[r]) - 1:
                right = int(inputs[r][c + 1])

            cell_value = int(inputs[r][c])
            # print(r, c, up, down, left, right)
            if up > cell_value and down > cell_value and left > cell_value and right > cell_value:
                total_risk += cell_value + 1
                print(r, c, up, down, left, right)
    return total_risk


def b(inputs):
    return


with open('inputs/09in.txt', 'r') as infile:
    inputs = infile.read()

# inputs = test_inputs
inputs = inputs.split('\n')
inputs = list(map(list, inputs))
print(a(inputs))
print(b(inputs))
