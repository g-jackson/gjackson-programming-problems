testinputs = [-6, +3, +8, +5, -6]

def a(inputs):
    i = 0
    for input in inputs:
        i += input
    return i


# Pretty damn slow
def b(inputs):
    i = 0
    prev = []
    while True:
        for input in inputs:
            i += input
            if i in prev:
                return i
            prev.append(i)

with open('inputs/01in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split()
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

print a(inputs)
print b(inputs)
#print tests
