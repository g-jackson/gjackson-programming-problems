test_inputs = '''3,4,3,1,2'''


def day_cycle(age_count, max_age, cycle_time):
    next_age_count = [0] * (max_age)
    for age in range(len(age_count)):
        # print(next_age_count)
        if age == 0:
            next_age_count[cycle_time - 1] += age_count[0]
            next_age_count[max_age - 1] += age_count[0]
        else:
            next_age_count[age - 1] += age_count[age]
    return next_age_count


def a(inputs):
    cycles = 80
    childhood = 2
    cycle_time = 7
    max_age = childhood + cycle_time
    age_count = [0] * (max_age)
    for fish in inputs:
        age_count[fish] += 1

    for i in range(cycles):
        age_count = day_cycle(age_count, max_age, cycle_time)
        print(i, sum(age_count), age_count)
    return sum(age_count)


def b(inputs):
    cycles = 256
    childhood = 2
    cycle_time = 7
    max_age = childhood + cycle_time
    age_count = [0] * (max_age)
    for fish in inputs:
        age_count[fish] += 1

    for i in range(cycles):
        age_count = day_cycle(age_count, max_age, cycle_time)
        # print(i, sum(age_count), age_count)
    return sum(age_count)


with open('inputs/06in.txt', 'r') as infile:
    inputs = infile.read()

# inputs = test_inputs
inputs = list(map(int, inputs.split(',')))

print(a(inputs))
print(b(inputs))
