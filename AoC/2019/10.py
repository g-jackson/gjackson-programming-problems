import math
import functools

testinputs = """.#..#
.....
#####
....#
...##"""

testinputs1 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

testinputs = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""


def a(inputs):
    asteroid_field = []
    for line in inputs.split():
        row = []
        for character in line:
            if character == ".":
                row.append(0)
            else:
                row.append(1)
        asteroid_field.append(row)
    
    asteroids = []
    for row in range(len(asteroid_field)):
        for column in range(len(asteroid_field[row])):
            if asteroid_field[row][column]:
                asteroids.append((column,row))
    
    max_score = 0
    max_point = None
    for asteroid in asteroids:
        num_detected = len(asteroids_detected(asteroid, asteroids)) - 1
        #print(asteroid, detected)
        if num_detected > max_score:
            max_point = asteroid
            max_score = num_detected
    return max_score, max_point


def asteroids_detected(asteroid, asteroids):
    asteroids = asteroids.copy()
    for target in asteroids:
        for other_target in asteroids:
            if target != other_target and target != asteroid and other_target != asteroid:
                if is_colinear(asteroid, target, other_target):
                    if not math.isclose(distance(asteroid, target) + distance(asteroid, other_target), distance(target, other_target)):
                        #print("collinear", asteroid, target, other_target, "removing", other_target)
                        asteroids.remove(other_target)
    return asteroids


def distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)


def is_colinear(a, b, c):
    return not a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])


def b(inputs):
    asteroid_field = []
    for line in inputs.split():
        row = []
        for character in line:
            if character == ".":
                row.append(0)
            else:
                row.append(1)
        asteroid_field.append(row)
    
    asteroids = []
    for row in range(len(asteroid_field)):
        for column in range(len(asteroid_field[row])):
            if asteroid_field[row][column]:
                asteroids.append((column,row))
    
    max_score = 0
    max_point = None
    for asteroid in asteroids:
        num_detected = len(asteroids_detected(asteroid, asteroids)) - 1
        #print(asteroid, detected)
        if num_detected > max_score:
            max_point = asteroid
            max_score = num_detected
    
    order = sorted(asteroids_detected(max_point, asteroids), key=functools.cmp_to_key(compare))
    return order

def compare(a, b):
    return (a[0] - 31) * (b[1] - 20) - (b[0] - 31) * (a[1] - 20)


with open('inputs/10in.txt', 'r') as infile:
    inputs = infile.read()


#print(a(testinputs))
#print(a(inputs))

print(b(inputs))
