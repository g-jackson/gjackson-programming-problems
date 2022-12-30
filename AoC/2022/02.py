def a(inputs):
    total = 0
    for i in inputs:
        them, us = i.split(' ')
        if us == 'X':
            total += 1
            if them == 'A':
                total += 3
            if them == 'B':
                total += 0
            if them == 'C':
                total += 6
        if us == 'Y':
            total += 2
            if them == 'A':
                total += 6
            if them == 'B':
                total += 3
            if them == 'C':
                total += 0
        if us == 'Z':
            total += 3
            if them == 'A':
                total += 0
            if them == 'B':
                total += 6
            if them == 'C':
                total += 3
        print(i, total)
    return total

def b(inputs):
    total = 0
    for i in inputs:
        them, goal = i.split(' ')
        if them == 'A':
            if goal == 'X':
                total += (0 + 3)
            if goal == 'Y':
                total += (3 + 1)
            if goal == 'Z':
                total += (6 + 2)
        if them == 'B':
            if goal == 'X':
                total += (0 + 1)
            if goal == 'Y':
                total += (3 + 2)
            if goal == 'Z':
                total += (6 + 3)
        if them == 'C':
            if goal == 'X':
                total += (0 + 2)
            if goal == 'Y':
                total += (3 + 3)
            if goal == 'Z':
                total += (6 + 1)
        print(i, total)
    return total

input_file = 'inputs/02test.txt'
input_file = 'inputs/02in.txt'

with open(input_file, 'r') as infile:
    inputs = infile.read()

inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
