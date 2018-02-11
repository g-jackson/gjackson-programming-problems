from itertools import permutations

sample1='''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.'''

def readinput(intext):
    guests = {}
    intext = intext.split('\n')
    for line in intext:
        split = line.split()
        guesta = split[0]
        guestb = split[-1][:-1]
        multiplier = split[2]
        if multiplier == "gain":
            multiplier = 1
        else:
            multiplier = -1
        value = split[3]
        if guesta not in guests:
            guests[guesta] = {}
        guests[guesta][guestb] = multiplier*(int)(value)
    return guests

def solve1(intext):
    guests = readinput(intext)
    highscore = 0
    for permutation in permutations(guests):
        #print permutation
        score = 0
        for guest in range(len(permutation)):
            left = permutation[guest-2]
            middle = permutation[guest-1]
            right = permutation[guest]
            #print middle, "is beside", left, guests[middle][left], "and", right, guests[middle][right]
            score += guests[middle][right] + guests[middle][left]

        if score > highscore:
            path = permutation
            highscore = score
    print path
    return highscore


def solve2(intext):
    guests = readinput(intext)
    guests["me"] = {}
    for guest in guests:
        guests["me"][guest] = 0
        guests[guest]["me"] = 0

    highscore = 0
    for permutation in permutations(guests):
        #print permutation
        score = 0
        for guest in range(len(permutation)):
            left = permutation[guest-2]
            middle = permutation[guest-1]
            right = permutation[guest]
            #print middle, "is beside", left, guests[middle][left], "and", right, guests[middle][right]
            score += guests[middle][right] + guests[middle][left]

        if score > highscore:
            path = permutation
            highscore = score
    print path
    return highscore 


with open('inputs/13in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests

#print solve1(tests)
print solve2(tests)
