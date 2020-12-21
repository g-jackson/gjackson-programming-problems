test_inputs = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''


def a(inputs):
    adapters = []
    for line in inputs:
        adapters.append(int(line))
    adapters.sort()
    differences = [0, 0, 1]
    prev = 0
    for adapter in adapters:
        differences[adapter - prev - 1] += 1
        prev = adapter
    # print(adapters, differences)
    return differences[0] * (differences[2])


def b(inputs):
    adapters = []
    for line in inputs:
        adapters.append(int(line))
    adapters.append(0)
    adapters.append(max(adapters) + 3)
    adapters.sort()
    print(adapters)
    valid_arrangements = {}
    for adapter in adapters:
        product = 0
        for i in range(1, 4):
            if adapter - i in adapters:
                print(adapter, '<-', adapter - i, product)
                product += valid_arrangements[adapter - i]
        if adapter == 0:
            product = 1
        valid_arrangements[adapter] = product
        print(valid_arrangements)
    return valid_arrangements[adapters[-1]]


with open('inputs/10in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
