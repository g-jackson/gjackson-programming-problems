sample1='''11'''
def solve1(intext):
    oldstring = intext
    newstring = ""
    for i in range(40):
        prev = oldstring[0]
        counter = 1
        newstring = ""
        for char in range(1,len(oldstring)):
            #print oldstring[char]
            if oldstring[char] == prev:
                counter += 1
            else:
                newstring += (str)(counter) + oldstring[char-1]
                counter = 1
                prev = oldstring[char]
        newstring += (str)(counter) + oldstring[char]
        #print newstring
        oldstring = newstring[:]
    return len(newstring)

def solve2(intext):
    oldstring = intext
    newstring = ""
    for i in range(50):
        prev = oldstring[0]
        counter = 1
        newstring = ""
        for char in range(1,len(oldstring)):
            #print oldstring[char]
            if oldstring[char] == prev:
                counter += 1
            else:
                newstring += (str)(counter) + oldstring[char-1]
                counter = 1
                prev = oldstring[char]
        newstring += (str)(counter) + oldstring[char]
        #print newstring
        oldstring = newstring[:]
    return len(newstring)


with open('inputs/10in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests

print solve1(tests)
print solve2(tests)
