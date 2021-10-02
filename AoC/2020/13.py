from numpy import triu_indices


test_inputs = '''939
7,13,x,x,59,x,31,19'''.split('\n')


def a(inputs):
    start_time = int(inputs[0])
    busses = inputs[1].split(',')
    bus_list = []
    scores = []
    for bus in busses:
        if bus != 'x':
            bus_id = int(bus)
            bus_list.append(bus_id)
            next_time = ((start_time // bus_id) + 1) * bus_id
            wait_time = next_time - start_time
            scores.append(wait_time)
    low = min(scores)
    low_bus = bus_list[scores.index(low)]
    return low * low_bus


def b(inputs):
    busses = inputs[1].split(',')
    delay_dict = {}
    for bus in busses:
        if bus != 'x':
            bus_id = bus
            delay_dict[int(bus_id)] = busses.index(bus_id)
    time = delay_dict
    print(time)

    interval = max(delay_dict.keys())
    time = interval + delay_dict[interval]
    found = False
    while not found:
        print(time)
        success = True
        time += interval
        for bus in delay_dict:
            if bus % time != 0:
                success = False
                break
        if success:
            found = True
            # print(time)



with open('inputs/13in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(test_inputs))
