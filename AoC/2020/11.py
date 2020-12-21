from copy import deepcopy
test_inputs = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''


def read_grid(inputs):
    grid = []
    grid.append([','] * (len(inputs[0]) + 2))
    for line in range(len(inputs)):
        grid.append([','])
        for char in inputs[line]:
            grid[line + 1].append(char)
        grid[line + 1].append(',')
    grid.append([','] * (len(inputs[0]) + 2))
    return grid


def print_grid(grid):
    for line in grid:
        print(''.join(line))


def count_occupied(grid):
    sum = 0
    for line in grid:
        sum += line.count('#')
    return sum


def count_adjacency(grid, x, y):
    return (int(grid[x + 1][y + 1] == '#') +
            int(grid[x + 1][y - 1] == '#') +
            int(grid[x + 1][y + 0] == '#') +
            int(grid[x + 0][y + 1] == '#') +
            int(grid[x + 0][y - 1] == '#') +
            int(grid[x - 1][y + 1] == '#') +
            int(grid[x - 1][y + 0] == '#') +
            int(grid[x - 1][y - 1] == '#'))


def check_direction(grid, x, y, offset_x, offset_y):
    while True:
        x += offset_x
        y += offset_y
        if grid[x][y] == ',' or grid[x][y] == 'L':
            return False
        if grid[x][y] == '#':
            return True


def count_directions(grid, x, y):
    return (int(check_direction(grid, x, y, 1, 1)) +
            int(check_direction(grid, x, y, 1, 0)) +
            int(check_direction(grid, x, y, 1, -1)) +
            int(check_direction(grid, x, y, 0, 1)) +
            int(check_direction(grid, x, y, 0, -1)) +
            int(check_direction(grid, x, y, -1, 1)) +
            int(check_direction(grid, x, y, -1, 0)) +
            int(check_direction(grid, x, y, -1, -1)))


def a(inputs):
    grid = read_grid(inputs)
    # print_grid(grid)
    done = False
    count = 0
    while not done:
        count += 1
        new_grid = deepcopy(grid)
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] != '.' and grid[x][y] != ',':
                    if grid[x][y] == '#' and count_adjacency(grid, x, y) >= 4:
                        new_grid[x][y] = 'L'
                    if grid[x][y] == 'L' and count_adjacency(grid, x, y) == 0:
                        new_grid[x][y] = '#'
        # print_grid(new_grid)
        # print(count_occupied(grid))
        if grid == new_grid:
            done = True
        grid = new_grid
        # print(count)
    return count_occupied(grid)


def b(inputs):
    grid = read_grid(inputs)
    # print_grid(grid)
    done = False
    count = 0
    while not done:
        count += 1
        adjacencies = []

        new_grid = deepcopy(grid)
        for x in range(len(grid)):
            adjacencies.append([])
            for y in range(len(grid[x])):
                if grid[x][y] != '.' and grid[x][y] != ',':
                    adjacencies[x].append(str(count_directions(grid, x, y)))

                    if grid[x][y] == '#' and count_directions(grid, x, y) >= 5:
                        new_grid[x][y] = 'L'
                    if grid[x][y] == 'L' and count_directions(grid, x, y) == 0:
                        new_grid[x][y] = '#'
                else:
                    adjacencies[x].append('.')
        # print_grid(adjacencies)
        # print_grid(new_grid)
        # print(count_occupied(grid))
        if grid == new_grid:
            done = True
        grid = new_grid
    return count_occupied(grid)


with open('inputs/11in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
