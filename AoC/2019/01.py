testinputs = [12, 14, 1969, 100756]

def calculate_fuel(mass):
    return mass//3 -2


def a(inputs):
    total = 0
    for input in inputs:
        total += calculate_fuel(input)
    return total


def b(inputs):
    total = 0
    for input in inputs:
        fuel_sum = 0
        fuel_added = input
        while calculate_fuel(fuel_added) > 0:
            fuel_added = calculate_fuel(fuel_added)
            fuel_sum += fuel_added
        print(input, fuel_sum)
        total += fuel_sum
    return total


with open('inputs/01in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split()
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

#print(a(inputs))
print(b(inputs))
#print tests
