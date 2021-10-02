test_inputs = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''

test_inputs2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''


def a(inputs):
    inputs = inputs.split('mask = ')[1:]
    memory = {}
    for task in inputs:
        mask = list(task.split('\n')[0])
        for write in task.split('\n')[1:]:
            if write:
                addr = write.split('mem[')[1].split(']')[0]
                val = list('{:036b}'.format(int(write.split('= ')[1])))
                init = ['0'] * 36
                for i, _ in enumerate(init):
                    if mask[i] != 'X':
                        init[i] = mask[i]
                    else:
                        init[i] = val[i]
                memory[addr] = int(''.join(init), 2)
            # print('val', val)
            # print('msk', mask)
            # print('out', init)
    total = 0
    for init in memory:
        total += memory[init]

    return total


def bin_tree(addr, pos, out_str, value, memory):
    if pos == 36:
        memory[out_str] = value
    else:
        if addr[pos] != 'X':
            bin_tree(addr, pos + 1, out_str + addr[pos], value, memory)
        else:
            bin_tree(addr, pos + 1, out_str + '1', value, memory)
            bin_tree(addr, pos + 1, out_str + '0', value, memory)


def b(inputs):
    inputs = inputs.split('mask = ')[1:]
    memory = {}
    for task in inputs:
        # print(task)
        mask = list(task.split('\n')[0])
        for write in task.split('\n')[1:]:
            if write:
                addr = list('{:036b}'.format(int(write.split('mem[')[1].split(']')[0])))
                out_addrs = addr.copy()
                val = int(write.split('= ')[1])
                for i, _ in enumerate(addr):
                    if mask[i] == 'X':
                        out_addrs[i] = 'X'
                    elif mask[i] == '1':
                        out_addrs[i] = '1'
                    else:
                        out_addrs[i] = addr[i]
                # print('add', addr)
                # print('msk', mask)
                # print('out', out_addrs)
                bin_tree(out_addrs, 0, '', val, memory)

    total = 0
    for init in memory:
        total += memory[init]
    return total


with open('inputs/14in.txt', 'r') as infile:
    inputs = infile.read()

print(a(inputs))
print(b(inputs))
