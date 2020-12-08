testinput = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def a(inputs, move_x, move_y):
    tree_count = 0
    width = len(inputs[0])
    height = len(inputs)
    # print(width, height)
    full_path = ''.join(inputs)
    pos_x = 0
    pos_y = 0
    for i in range(round(height / move_y) - 1):
        pos_x = (pos_x + move_x) % width
        pos_y += move_y
        # print(pos_x, pos_y, full_path[pos_x + width * pos_y])
        if full_path[pos_x + width * pos_y] == '#':
            tree_count += 1
    return tree_count


def b(inputs):
    return a(inputs, 1, 1) * a(inputs, 3, 1) * a(inputs, 5, 1) * a(inputs, 7, 1) * a(inputs, 1, 2)


with open('inputs/03in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

# print(a(testinput.split('\n')))
print(a(inputs, 3, 1))
# print(b(testinput.split('\n')))
print(b(inputs))
