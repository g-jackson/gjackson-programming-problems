test_inputs = '''0,3,6'''.split(',')


def a(inputs, max_time):
    spoken = {}
    time = 1
    current = 0
    # Starting numbers
    for number in inputs:
        spoken[int(number)] = time
        current = number
        # print(time, current, spoken)
        time += 1
    current = 0
    while time < max_time:
        if current in spoken:
            new_current = time - spoken[current]
            # print('time', time, '-', spoken[current], 'spoken', new_current)
        else:
            new_current = 0
        spoken[current] = time
        current = new_current
        # print(time, current, spoken)
        time += 1
    return current


def b(inputs, max_time):
    return a(inputs, max_time)


with open('inputs/15in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split(',')

print(a(inputs, 2020))
print(b(inputs, 30000000))
