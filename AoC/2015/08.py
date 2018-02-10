sample1='''""
"abc"
"aaa\"aaa"
"\x27"'''

def solve1(intext):
    acutalchars = len(intext)
    evalchars = 0
    split = intext.split()
    for line in split:
        evalchars += len(eval(line))
    evalchars += len(split) - 1 # Add in newline chars removed by split
    return acutalchars - evalchars

def solve2(intext):
    addedchars = 0
    split = intext.split()
    for line in split:
        addedchars += 2 + line.count('\\') + line.count('"')
    return addedchars


with open('inputs/08in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests

print solve1(tests)
print solve2(tests)
