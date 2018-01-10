sample1 ='''3'''


def solve1(rotations):
    spins = 2017
    #spins = 9
    spinlock = [0]
    current = 1
    for i in range(spins):
        current = (current + rotations) % len(spinlock)
        #print current
        spinlock.insert(current+1,i+1)
        current = current + 1
        #print spinlock
    return spinlock[current+1]

def solve2(rotations):
    spins = 50000000
    #spins = 9
    size = 1
    current = 1
    result = 0
    for i in range(spins):
        current = (current + rotations) % size
        if current == 0:
            #print i + 1
            result = i + 1
        current = current + 1
        size = size + 1

    return result

#test = 3
test = 329

#print test
#print solve1(test)
print solve2(test)

