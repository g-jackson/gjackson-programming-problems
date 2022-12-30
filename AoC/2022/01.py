def a(inputs):
    cals = []
    for i in inputs:
        lines = i.split('\n')
        cals.append(sum(map(int, lines)))
    return max(cals)

def b(inputs):
    cals = []
    for i in inputs:
        lines = i.split('\n')
        cals.append(sum(map(int, lines)))
    cals.sort()
    return sum(cals[-3:])

# with open('inputs/01test.txt', 'r') as infile:
with open('inputs/01in.txt', 'r') as infile:
    inputs = infile.read()

inputs = inputs.split('\n\n')

print(a(inputs))
print(b(inputs))
