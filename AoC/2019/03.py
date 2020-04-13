

testinputs = [["R8","U5","L5","D3"], ["U7","R6","D4","L4"]]
#testinputs = [["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"], ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]]
#testinputs =  [['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'], ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']]


def get_wire_points(wire):
    wire_points = []
    current_point = (0, 0)
    distance = 1
    for point in wire:
        if point[0] == "U":
            for _ in range(int(point[1:])):
                current_point = (current_point[0], current_point[1] + 1, distance)
                wire_points.append(current_point)
                distance += 1
        elif point[0] == "D":
            for _ in range(int(point[1:])):
                current_point = (current_point[0], current_point[1] - 1, distance)
                wire_points.append(current_point)
                distance += 1
        elif point[0] == "R":
            for _ in range(int(point[1:])):
                current_point = (current_point[0] + 1, current_point[1], distance)
                wire_points.append(current_point)
                distance += 1
        elif point[0] == "L":
            for _ in range(int(point[1:])):
                current_point = (current_point[0] - 1, current_point[1], distance)
                wire_points.append(current_point)
                distance += 1
    return wire_points


def get_intersections(wire_points1, wire_points2):
    return list(set([point[0:2] for point in wire_points1]).intersection(set([point[0:2] for point in wire_points2])))


def get_closest_intersection_a(intersections):
    closest_distance = abs(intersections[0][0]) + abs(intersections[0][1])
    for intersection in intersections:
        if abs(intersection[0]) + abs(intersection[1]) < closest_distance:
            closest_distance = abs(intersection[0]) + abs(intersection[1])
    return closest_distance


def get_closest_intersection_b(wire_points1, wire_points2, intersections):
    distances = []
    for intersection in intersections:
        min1 = 100000000
        min2 = 100000000
        for point in wire_points1:
            if (point[0:2] == intersection):
                min1 = min(point[2], min1)
        for point in wire_points2:
            if (point[0:2] == intersection):
                min2 = min(point[2], min2)
        
        #print(intersection, min1, min2, min1+min2)
        distances.append(min1+min2)
    return min(distances)


def a(inputs):
    wire1 = inputs[0]
    wire2 = inputs[1]
    wire_points1 = get_wire_points(wire1)
    wire_points2 = get_wire_points(wire2) 
    intersections = get_intersections(wire_points1, wire_points2)
    print(intersections)
    return get_closest_intersection_a(intersections)

def b(inputs):
    wire1 = inputs[0]
    wire2 = inputs[1]
    wire_points1 = get_wire_points(wire1)
    wire_points2 = get_wire_points(wire2) 
    intersections = get_intersections(wire_points1, wire_points2)
    print(intersections)
    return get_closest_intersection_b(wire_points1, wire_points2, intersections)


with open('inputs/03in.txt',  'r') as infile:
    inputs = infile.read()
inputs = inputs.split()
for i in range(len(inputs)):
    inputs[i] = inputs[i].split(",")

#print(inputs)
#print(a(inputs))
print(b(inputs))
#print tests
