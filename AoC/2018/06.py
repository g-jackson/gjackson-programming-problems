testinputs = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

def a(inputs):
    points = []
    for i in inputs:
        points.append((int(i.split(", ")[0]), int(i.split(", ")[1])))
    print(points)
    print(gen_perimeter(points))
    return inputs

def b(inputs):
    return


def gen_perimeter(points):
    x_max = points[0]
    x_min = points[0]
    y_max = points[0]
    y_min = points[0]
    for point in points:
        if point[0] > x_min[0]:
            x_min = point
        if point[0] < x_max[0]:
            x_max = point
        if point[1] > y_min[1]:
            y_min = point
        if point[1] < y_max[1]:
            y_max = point
    return x_max, x_min, y_max, y_min


with open('inputs/06in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split("\n")

print(a(testinputs.split("\n")))
print(b(inputs))
