def a(inputs):
    return

def b(inputs):
    return

input_file = 'inputs/00test.txt'
input_file = 'inputs/00in.txt'

with open(input_file, 'r') as infile:
    inputs = infile.read()

inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
