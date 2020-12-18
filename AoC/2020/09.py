
def a(inputs):
    total = 0
    return total


def b(inputs):
    total = 0
    return total


with open('inputs/09in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
