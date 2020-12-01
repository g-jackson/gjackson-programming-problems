
def a(inputs):
    for x in inputs:
        for y in inputs:
            if y + x == 2020:
                return x * y


def b(inputs):
    for x in inputs:
        for y in inputs:
            for z in inputs:
                if y + x + z == 2020:
                    return x * y * z


with open('inputs/01in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split()
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

print(a(inputs))
print(b(inputs))
