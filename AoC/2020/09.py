from itertools import combinations  
test_inputs = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''


def a(inputs):
    values = []
    for line in inputs:
        values.append(int(line))
    preamble = 25
    for i in range(len(values)):
        if i >= preamble:
            valid = False
            prev = values[i - 25: i]
            combos = combinations(prev, 2)
            for combo in combos:
                if combo[0] + combo[1] == values[i]:
                    valid = True
            if not valid:
                return values[i]
    return


def b(inputs, a_val):
    values = []
    for line in inputs:
        values.append(int(line))
    for i in range(len(values)):
        for j in range(i):
            # print(j, i, values[i - j:i])
            if sum(values[i - j:i]) == a_val:
                return max(values[i - j:i]) + min(values[i - j:i])
            if sum(values[i - j:i]) > a_val:
                break
    return


with open('inputs/09in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

a_val = a(inputs)
print(a_val)
print(b(inputs, a_val))
