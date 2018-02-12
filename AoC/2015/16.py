sample1=''''''

def readinput():
    facts = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    return facts

def solve1(intext):
    #print intext
    facts = readinput()
    #print facts
    result = 0
    for line in intext:
        split = line.split()
        sue = split[1][:-1]
        elements = (len(split)/2)-1
        #print sue, len(split), elements, split
        valid = True
        for i in range(elements):
            key = split[2+(2*i)][:-1]
            value = (int)(split[3+(2*i)].replace(',', ''))
            if facts[key] != value:
                #print key, value, facts
                valid = False
        if valid:
            result = sue 
    return result

def solve2(intext):
    #print intext
    facts = readinput()
    #print facts
    result = 0
    for line in intext:
        split = line.split()
        sue = split[1][:-1]
        elements = (len(split)/2)-1
        #print sue, len(split), elements, split
        valid = True
        for i in range(elements):
            key = split[2+(2*i)][:-1]
            value = (int)(split[3+(2*i)].replace(',', ''))
            if key == "cats" or key == "trees":
                if facts[key] >= value:
                    valid = False
            elif key == "pomeranians" or key == "goldfish":
                if facts[key] <= value:
                    valid = False
            else:
                if facts[key] != value:   
                    valid = False
        if valid:
            #print split, facts
            result = sue 
    return result


with open('inputs/16in.txt','r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')

print solve1(tests)
print solve2(tests)
