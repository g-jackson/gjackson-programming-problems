testinputs = []


def a(inputs):
    return


def b(inputs):
    return


with open('inputs/11in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split()

for i in range(len(inputs)):
    inputs[i] = int(inputs[i])


print(a(testinputs))
#print(b(inputs))
#print tests
