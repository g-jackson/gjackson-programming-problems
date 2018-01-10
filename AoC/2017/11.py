from collections import Counter

def solve1(intext):
    intext = intext.split(',')
    counts = Counter(intext)
    print counts
    coord = [0,0,0]
    coord[0] = counts['n'] + counts['ne'] - counts['s'] - counts['sw']
    coord[1] = counts['sw'] + counts['nw'] - counts['ne'] - counts['se']
    coord[2] = counts['se'] + counts['s'] - counts['nw'] - counts['n']
    print coord

    distance = max(abs(coord[0]), abs(coord[1]),abs(coord[2]))
    print distance
    return 

def solve2(intext):
    intext = intext.split(',')
    max_distance = 0
    for i in range(len(intext)):
        journey = intext[0:i]
        counts = Counter(journey)
        #print counts
        coord = [0,0,0]
        coord[0] = counts['n'] + counts['ne'] - counts['s'] - counts['sw']
        coord[1] = counts['sw'] + counts['nw'] - counts['ne'] - counts['se']
        coord[2] = counts['se'] + counts['s'] - counts['nw'] - counts['n']
        #print coord

        distance = max(abs(coord[0]), abs(coord[1]),abs(coord[2]))
        #print distance
        if distance > max_distance:
            max_distance = distance
            #print max_distance
    return max_distance


with open('inputs/11in.txt', 'r') as infile:
    tests = infile.read()
#tests = 'ne,ne,ne'
print tests

print solve1(tests)
print solve2(tests)
