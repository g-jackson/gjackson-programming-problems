testinputs = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]


def a(inputs):
    sheet = set()
    collisions = set()
    for input in inputs:
        print(input)
        input = input.split(",")
        x = int(input[0].split(" ")[-1])
        y = int(input[1].split(":")[0])
        w = int(input[1].split(":")[1].split("x")[0])
        h = int(input[1].split("x")[1])
        print x, y, w, h
        add_entry_a(sheet, collisions, x, y, w, h)
    #print sheet
    return len(collisions)


def add_entry(sheet, collisions, x, y, w, h):
    for i in range(w):
        for j in range(h):
            point = (x + i, y + j)
            if point in sheet:
                collisions.add(point)
            else:
                sheet.add(point)
    return


def b(inputs):
    sheet = set()
    collisions = set()
    for entry in range(len(inputs)):
        input = inputs[entry]
        input = input.split(",")
        x = int(input[0].split(" ")[-1])
        y = int(input[1].split(":")[0])
        w = int(input[1].split(":")[1].split("x")[0])
        h = int(input[1].split("x")[1])
        add_entry(sheet, collisions, x, y, w, h)

    for entry in range(len(inputs)):
        input = inputs[entry]
        input = input.split(",")
        claim_id = input[0].split(" ")[0]
        x = int(input[0].split(" ")[-1])
        y = int(input[1].split(":")[0])
        w = int(input[1].split(":")[1].split("x")[0])
        h = int(input[1].split("x")[1])
        check_entry(claim_id, sheet, collisions, x, y, w, h)


def check_entry(entry, sheet, collisions, x, y, w, h):
    valid = True
    for i in range(w):
        for j in range(h):
            point = (x + i, y + j)
            if point in collisions:
                valid = False
    if valid:
        print(entry)
        return valid


with open('inputs/03in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split("\n")


print(a(inputs))
print(b(inputs))
