
def a(inputs):
    pass


def b(inputs):
    pass


with open('inputs/03in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
