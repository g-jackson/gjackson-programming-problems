sample1='''Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.'''

def readinput(intext):
    positions = []
    start = []
    for line in intext:
        positions.append((int)(line.split(' ')[3]))
        start.append((int)(line.split(' ')[-1][:-1]))
    return positions, start

def solve1(intext):
    positions, start = readinput(intext)
    print positions, start
    done = False
    time = 0
    while not done:
        valid = True
        for disc in range(len(positions)):
            if  (start[disc]+ 1 + time + disc) % positions[disc] != 0:
                valid = False
        if valid:
            done = True
        else:
            time = time + 1
    return time

def solve2(intext):
    positions, start = readinput(intext)
    positions.append(11)
    start.append(0)
    print positions, start
    done = False
    time = 0
    while not done:
        valid = True
        for disc in range(len(positions)):
            if  (start[disc]+ 1 + time + disc) % positions[disc] != 0:
                valid = False
        if valid:
            done = True
        else:
            time = time + 1
    return time


with open('inputs/15in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')
print tests

#print solve1(tests)
print solve2(tests)
