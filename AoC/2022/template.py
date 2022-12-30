def a(inputs):
    return

def b(inputs):
    return

input_file = 'inputs/02test.txt'
input_file = 'inputs/02in.txt'

with open(input_file, 'r') as infile:
    inputs = infile.read()

print(a(inputs))
print(b(inputs))
