test_inputs = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''


def a(inputs):
    pipes = []
    for line in inputs:
        source = list(map(int, line.split(' -> ')[0].split(',')))
        target = list(map(int, line.split(' -> ')[1].split(',')))
        # Only use straight pipes
        if source[0] == target[0] or source[1] == target[1]:
            pipes.append([source, target])

    grid = {}
    collisions = 0

    for pipe in pipes:
        # print(pipe)
        source = pipe[0]
        target = pipe[1]
        if source[0] == target[0]:
            for i in range(min(source[1], target[1]), max(source[1], target[1]) + 1):
                if (source[0], i) in grid:
                    if grid[(source[0], i)] == 1:
                        collisions += 1
                    grid[(source[0], i)] += 1
                else:
                    grid[(source[0], i)] = 1

        if source[1] == target[1]:
            for i in range(min(source[0], target[0]), max(source[0], target[0]) + 1):
                if (i, source[1]) in grid:
                    if grid[i, source[1]] == 1:
                        collisions += 1
                    grid[i, source[1]] += 1

                else:
                    grid[i, source[1]] = 1
        # print(grid)
    return collisions


def addToGrid(grid, point):
    collision = 0
    if point in grid:
        if grid[point] == 1:
            collision = 1
        grid[point] += 1
    else:
        grid[point] = 1
    # print(point, collision)
    return collision


def b(inputs):
    pipes = []
    for line in inputs:
        source = list(map(int, line.split(' -> ')[0].split(',')))
        target = list(map(int, line.split(' -> ')[1].split(',')))
        pipes.append([source, target])

    grid = {}
    collisions = 0
    for pipe in pipes:
        # print(pipe)
        source = pipe[0]
        target = pipe[1]
        # Vertical
        if source[0] == target[0]:
            for i in range(min(source[1], target[1]), max(source[1], target[1]) + 1):
                collisions += addToGrid(grid, (source[0], i))
        # Horizontal
        elif source[1] == target[1]:
            for i in range(min(source[0], target[0]), max(source[0], target[0]) + 1):
                collisions += addToGrid(grid, (i, source[1]))
        # Diagonal
        else:
            if source[0] > target[0]:
                x_direction = -1
            else:
                x_direction = 1
            if source[1] > target[1]:
                y_direction = -1
            else:
                y_direction = 1
            for i in range(abs(source[0] - target[0]) + 1):
                collisions += addToGrid(grid, (source[0] + (x_direction * i), source[1] + (y_direction * i)))

        # print(grid)
    return collisions


with open('inputs/05in.txt', 'r') as infile:
    inputs = infile.read()

# inputs = test_inputs
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
