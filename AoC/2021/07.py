test_inputs = '''16,1,2,0,4,2,7,1,2,14'''


def a(inputs):
    min_fuel = max(inputs) * len(inputs)
    for i in range(max(inputs) + 1):
        total_cost = 0
        for move in inputs:
            total_cost += abs(i - move)
        if total_cost < min_fuel:
            min_fuel = total_cost
    return min_fuel


def b(inputs):
    fuel_costs = []
    for i in range(max(inputs) + 1):
        total_cost = 0
        for move in inputs:
            total_cost += sum(range(abs(i - move) + 1))
        fuel_costs.append(total_cost)
    return min(fuel_costs)


with open('inputs/07in.txt', 'r') as infile:
    inputs = infile.read()

# inputs = test_inputs
inputs = list(map(int, inputs.split(',')))

print(a(inputs))
print(b(inputs))
