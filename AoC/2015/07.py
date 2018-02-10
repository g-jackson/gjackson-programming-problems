sample1='''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''

def readinstruction(split, wires):
    ina = ''
    inb = '0'
    op = ''
    if len(split) == 5:
        ina = split[0]
        inb = split[2]
        op = split[1]
    elif len(split) == 4:
        ina = split[1]
        op = split[0]
    else:
        ina = split[0]
        op = "ASSIGN"
    if ina.isalpha():
        if ina in wires:
            ina = wires[ina]
        else:
            op = "DEFER"
    else:
        ina = (int)(ina)
    if inb.isalpha():
        if inb in wires:
            inb = wires[inb]
        else:
            op = "DEFER"
    else:
        inb = (int)(inb)
    return ina , inb, op

def solve1(intext):
    wires = {}
    rules = intext[:]
    result = 0
    while len(rules) != 0:
        for line in rules:
            #print line
            split = line.split()
            wire = split[-1]
            ina , inb, op = readinstruction(split, wires)
            if op == "ASSIGN":
                wires[wire] = ina
            if op == "NOT":
                wires[wire] = ~ina
            if op == "AND":
                 wires[wire] = ina & inb
            if op == "OR":
                 wires[wire] = ina | inb
            if op == "LSHIFT":
                 wires[wire] = ina << inb
            if op == "RSHIFT":
                 wires[wire] = ina >> inb
            if op != "DEFER":
                rules.remove(line)

    for wire in wires:
        if wires[wire] > 0:
            if wire == 'a':
                result = wires[wire]
            #print wire, wires[wire]
        else:
            if wire == 'a':
                result = 65535 + wires[wire] + 1
            #print wire, 65535 + wires[wire] + 1

    return result


def solve2(intext, aresult):
    wires = {'b':aresult}
    rules = intext[:]
    result = 0
    while len(rules) != 0:
        for line in rules:
            #print line
            split = line.split()
            wire = split[-1]
            ina , inb, op = readinstruction(split, wires)
            if op == "ASSIGN":
                if wire != 'b':
                    wires[wire] = ina
            if op == "NOT":
                wires[wire] = ~ina
            if op == "AND":
                 wires[wire] = ina & inb
            if op == "OR":
                 wires[wire] = ina | inb
            if op == "LSHIFT":
                 wires[wire] = ina << inb
            if op == "RSHIFT":
                 wires[wire] = ina >> inb
            if op != "DEFER":
                rules.remove(line)

    for wire in wires:
        if wires[wire] > 0:
            if wire == 'a':
                result = wires[wire]
            #print wire, wires[wire]
        else:
            if wire == 'a':
                result = 65535 + wires[wire] + 1
            #print wire, 65535 + wires[wire] + 1

    return result


with open('inputs/07in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')

a = solve1(tests)
print a
print solve2(tests,a)
