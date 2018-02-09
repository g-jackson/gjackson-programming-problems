sample1='''(())'''

def solve1(intext):
    return intext.count('(') - intext.count(')')

def solve2(intext):
    count = 0
    result = 0
    for i in range(len(intext)):
        if intext[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return i + 1
    return 


with open('inputs/01in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1

#print tests

print solve1(tests)
print solve2(tests)
