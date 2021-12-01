test_inputs = '''.#.
..#
###'''.split('\n')

ITERATIONS = 6


def add_score_to_neighbours_a(neighbour_scores, x, y, z):
    add_score_a(neighbour_scores, x + 1, y, z)
    add_score_a(neighbour_scores, x - 1, y, z)

    add_score_a(neighbour_scores, x, y + 1, z)
    add_score_a(neighbour_scores, x, y - 1, z)

    add_score_a(neighbour_scores, x, y, z + 1)
    add_score_a(neighbour_scores, x, y, z - 1)

    add_score_a(neighbour_scores, x + 1, y + 1, z)
    add_score_a(neighbour_scores, x - 1, y + 1, z)
    add_score_a(neighbour_scores, x + 1, y - 1, z)
    add_score_a(neighbour_scores, x - 1, y - 1, z)

    add_score_a(neighbour_scores, x, y + 1, z + 1)
    add_score_a(neighbour_scores, x, y + 1, z - 1)
    add_score_a(neighbour_scores, x, y - 1, z + 1)
    add_score_a(neighbour_scores, x, y - 1, z - 1)

    add_score_a(neighbour_scores, x + 1, y, z + 1)
    add_score_a(neighbour_scores, x + 1, y, z - 1)
    add_score_a(neighbour_scores, x - 1, y, z + 1)
    add_score_a(neighbour_scores, x - 1, y, z - 1)

    add_score_a(neighbour_scores, x + 1, y + 1, z + 1)
    add_score_a(neighbour_scores, x + 1, y + 1, z - 1)
    add_score_a(neighbour_scores, x + 1, y - 1, z + 1)
    add_score_a(neighbour_scores, x + 1, y - 1, z - 1)

    add_score_a(neighbour_scores, x - 1, y + 1, z + 1)
    add_score_a(neighbour_scores, x - 1, y + 1, z - 1)
    add_score_a(neighbour_scores, x - 1, y - 1, z + 1)
    add_score_a(neighbour_scores, x - 1, y - 1, z - 1)


def add_score_to_neighbours_b(neighbour_scores, w, x, y, z):
    # Neater / scaling solution using for range(1, 3**dimensions) -> ternary string, cast each char as int add to relevant position
    add_score_b(neighbour_scores, w + 1, x, y, z)
    add_score_b(neighbour_scores, w - 1, x, y, z)

    add_score_b(neighbour_scores, w, x + 1, y, z)
    add_score_b(neighbour_scores, w, x - 1, y, z)

    add_score_b(neighbour_scores, w, x, y + 1, z)
    add_score_b(neighbour_scores, w, x, y - 1, z)

    add_score_b(neighbour_scores, w, x, y, z + 1)
    add_score_b(neighbour_scores, w, x, y, z - 1)

    add_score_b(neighbour_scores, w, x + 1, y + 1, z)
    add_score_b(neighbour_scores, w, x - 1, y + 1, z)
    add_score_b(neighbour_scores, w, x + 1, y - 1, z)
    add_score_b(neighbour_scores, w, x - 1, y - 1, z)

    add_score_b(neighbour_scores, w, x, y + 1, z + 1)
    add_score_b(neighbour_scores, w, x, y + 1, z - 1)
    add_score_b(neighbour_scores, w, x, y - 1, z + 1)
    add_score_b(neighbour_scores, w, x, y - 1, z - 1)

    add_score_b(neighbour_scores, w, x + 1, y, z + 1)
    add_score_b(neighbour_scores, w, x + 1, y, z - 1)
    add_score_b(neighbour_scores, w, x - 1, y, z + 1)
    add_score_b(neighbour_scores, w, x - 1, y, z - 1)

    add_score_b(neighbour_scores, w, x + 1, y + 1, z + 1)
    add_score_b(neighbour_scores, w, x + 1, y + 1, z - 1)
    add_score_b(neighbour_scores, w, x + 1, y - 1, z + 1)
    add_score_b(neighbour_scores, w, x + 1, y - 1, z - 1)

    add_score_b(neighbour_scores, w, x - 1, y + 1, z + 1)
    add_score_b(neighbour_scores, w, x - 1, y + 1, z - 1)
    add_score_b(neighbour_scores, w, x - 1, y - 1, z + 1)
    add_score_b(neighbour_scores, w, x - 1, y - 1, z - 1)

    add_score_b(neighbour_scores, w + 1, x + 1, y, z)
    add_score_b(neighbour_scores, w + 1, x - 1, y, z)

    add_score_b(neighbour_scores, w + 1, x, y + 1, z)
    add_score_b(neighbour_scores, w + 1, x, y - 1, z)

    add_score_b(neighbour_scores, w + 1, x, y, z + 1)
    add_score_b(neighbour_scores, w + 1, x, y, z - 1)

    add_score_b(neighbour_scores, w + 1, x + 1, y + 1, z)
    add_score_b(neighbour_scores, w + 1, x - 1, y + 1, z)
    add_score_b(neighbour_scores, w + 1, x + 1, y - 1, z)
    add_score_b(neighbour_scores, w + 1, x - 1, y - 1, z)

    add_score_b(neighbour_scores, w + 1, x, y + 1, z + 1)
    add_score_b(neighbour_scores, w + 1, x, y + 1, z - 1)
    add_score_b(neighbour_scores, w + 1, x, y - 1, z + 1)
    add_score_b(neighbour_scores, w + 1, x, y - 1, z - 1)

    add_score_b(neighbour_scores, w + 1, x + 1, y, z + 1)
    add_score_b(neighbour_scores, w + 1, x + 1, y, z - 1)
    add_score_b(neighbour_scores, w + 1, x - 1, y, z + 1)
    add_score_b(neighbour_scores, w + 1, x - 1, y, z - 1)

    add_score_b(neighbour_scores, w + 1, x + 1, y + 1, z + 1)
    add_score_b(neighbour_scores, w + 1, x + 1, y + 1, z - 1)
    add_score_b(neighbour_scores, w + 1, x + 1, y - 1, z + 1)
    add_score_b(neighbour_scores, w + 1, x + 1, y - 1, z - 1)

    add_score_b(neighbour_scores, w + 1, x - 1, y + 1, z + 1)
    add_score_b(neighbour_scores, w + 1, x - 1, y + 1, z - 1)
    add_score_b(neighbour_scores, w + 1, x - 1, y - 1, z + 1)
    add_score_b(neighbour_scores, w + 1, x - 1, y - 1, z - 1)

    add_score_b(neighbour_scores, w - 1, x + 1, y, z)
    add_score_b(neighbour_scores, w - 1, x - 1, y, z)

    add_score_b(neighbour_scores, w - 1, x, y + 1, z)
    add_score_b(neighbour_scores, w - 1, x, y - 1, z)

    add_score_b(neighbour_scores, w - 1, x, y, z + 1)
    add_score_b(neighbour_scores, w - 1, x, y, z - 1)

    add_score_b(neighbour_scores, w - 1, x + 1, y + 1, z)
    add_score_b(neighbour_scores, w - 1, x - 1, y + 1, z)
    add_score_b(neighbour_scores, w - 1, x + 1, y - 1, z)
    add_score_b(neighbour_scores, w - 1, x - 1, y - 1, z)

    add_score_b(neighbour_scores, w - 1, x, y + 1, z + 1)
    add_score_b(neighbour_scores, w - 1, x, y + 1, z - 1)
    add_score_b(neighbour_scores, w - 1, x, y - 1, z + 1)
    add_score_b(neighbour_scores, w - 1, x, y - 1, z - 1)

    add_score_b(neighbour_scores, w - 1, x + 1, y, z + 1)
    add_score_b(neighbour_scores, w - 1, x + 1, y, z - 1)
    add_score_b(neighbour_scores, w - 1, x - 1, y, z + 1)
    add_score_b(neighbour_scores, w - 1, x - 1, y, z - 1)

    add_score_b(neighbour_scores, w - 1, x + 1, y + 1, z + 1)
    add_score_b(neighbour_scores, w - 1, x + 1, y + 1, z - 1)
    add_score_b(neighbour_scores, w - 1, x + 1, y - 1, z + 1)
    add_score_b(neighbour_scores, w - 1, x + 1, y - 1, z - 1)

    add_score_b(neighbour_scores, w - 1, x - 1, y + 1, z + 1)
    add_score_b(neighbour_scores, w - 1, x - 1, y + 1, z - 1)
    add_score_b(neighbour_scores, w - 1, x - 1, y - 1, z + 1)
    add_score_b(neighbour_scores, w - 1, x - 1, y - 1, z - 1)


def add_score_a(neighbour_scores, x, y, z):
    if (x, y, z) in neighbour_scores:
        neighbour_scores[(x, y, z)] += 1
    else:
        neighbour_scores[(x, y, z)] = 1


def add_score_b(neighbour_scores, w, x, y, z):
    if (w, x, y, z) in neighbour_scores:
        neighbour_scores[(w, x, y, z)] += 1
    else:
        neighbour_scores[(w, x, y, z)] = 1


def calculate_new_actives(active, neighbour_scores):
    new_active = []
    for score in neighbour_scores:
        if score in active:
            if neighbour_scores[score] == 2 or neighbour_scores[score] == 3:
                new_active.append(score)
        else:
            if neighbour_scores[score] == 3:
                new_active.append(score)

    return new_active


def a(inputs):
    active = []
    for x, line in enumerate(inputs):
        for y, char in enumerate(line):
            if char == '#':
                active.append((x, y, 0))
    print(active)

    for iteration in range(ITERATIONS):
        print('Iteration: ', iteration)
        neighbour_scores = {}
        for node in active:
            add_score_to_neighbours_a(neighbour_scores, node[0], node[1], node[2])
        active = calculate_new_actives(active, neighbour_scores)
        print(len(active))
    return len(active)


def b(inputs):
    active = []
    for i, line in enumerate(inputs):
        for j, char in enumerate(line):
            if char == '#':
                active.append((0, i, j, 0))
    print(active)

    for iteration in range(ITERATIONS):
        print('Iteration: ', iteration)
        neighbour_scores = {}
        for node in active:
            add_score_to_neighbours_b(neighbour_scores, node[0], node[1], node[2], node[3])
        active = calculate_new_actives(active, neighbour_scores)
        # print(active)
        print(len(active))
    return len(active)


with open('inputs/17in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
