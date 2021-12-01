test_inputs1 = '''199
200
208
210
200
207
240
269
260
263'''


def a(inputs):
    count = -1
    current = 0
    for i in inputs:
        if i > current:
            count += 1
        current = i
    return count


def b(inputs):
    count = -1
    current = 0
    for i in range(len(inputs) - 2):
        window = (inputs[i] + inputs[i + 1] + inputs[i + 2])
        if window > current:
            count += 1
        current = window
    return count


with open('inputs/01in.txt', 'r') as infile:
    inputs = infile.read()
# inputs = test_inputs1
inputs = inputs.split('\n')
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

print(a(inputs))
print(b(inputs))
