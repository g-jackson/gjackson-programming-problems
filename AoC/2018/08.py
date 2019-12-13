testinputs = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"""
def a(inputs):
    print(inputs)
    return

def b(inputs):
    return


with open('inputs/08in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split()


print(a(testinputs.split()))
print(b(inputs))
