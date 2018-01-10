def solve1(steps):
    current = 0
    moves = 0
    notDone = True
    while(notDone):
        #print "current: ", current
        #print "moves: ", moves
        #print "steps: ", steps

        moves +=1
        currentpos = current
        current = steps[current] + current
        steps[currentpos] += 1
        if (current < 0) or (current >= len(steps)):
            notDone = False

    print "current: ", current
    print "moves: ", moves
    print "steps: ", steps
    return moves

def solve2(steps):
    current = 0
    moves = 0
    notDone = True
    while(notDone):
        #print "current: ", current
        #print "moves: ", moves
        #print "steps: ", steps
        moves +=1
        currentpos = current
        current = steps[current] + current
        if steps[currentpos] >= 3:
            steps[currentpos] -= 1
        else:
            steps[currentpos] =  steps[currentpos] + 1

        if (current < 0) or (current >= len(steps)):
            notDone = False

    return moves

with open('inputs/5in.txt', 'r') as infile:
    test = infile.read()
    test = [int(x) for x in list(test.split('\n'))]

#test = [0,3,0,1,-3]

print solve2(test)
