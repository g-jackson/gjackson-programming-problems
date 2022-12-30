def is_subset(a, b):
    if (a[0] <= b[0] and a[1] >= b[1]) or (a[0] >= b[0] and a[1] <= b[1]):
        return True
    return False


def is_overlap(a, b):
    if (a[0] < b[0] and a[1] < b[0]) or (a[0] > b[1] and a[0] > b[1]):
        return False
    return True


def a(inputs):
    total = 0
    for i in inputs:
        print(i)
        a_vals, b_vals = i.split(',')
        a = (int(a_vals.split('-')[0]), (int(a_vals.split('-')[1])))
        b = (int(b_vals.split('-')[0]), (int(b_vals.split('-')[1])))
        # print(a, b, is_subset(a, b))
        total += is_subset(a, b)
    return total


def b(inputs):
    total = 0
    for i in inputs:
        print(i)
        a_vals, b_vals = i.split(',')
        a = (int(a_vals.split('-')[0]), (int(a_vals.split('-')[1])))
        b = (int(b_vals.split('-')[0]), (int(b_vals.split('-')[1])))
        # print(a, b, is_overlap(a, b))
        total += is_overlap(a, b)
    return total


input_file = 'inputs/04test.txt'
input_file = 'inputs/04in.txt'

with open(input_file, 'r') as infile:
    inputs = infile.read()

inputs = inputs.split('\n')
print(a(inputs))
print(b(inputs))
