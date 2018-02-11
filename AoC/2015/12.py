import re

sample1=''''''

def solve1(intext):
    removed = re.findall('-?[0-9]\d*',intext)
    removed = map(int, removed)
    #print removed
    return sum(removed)

def solve2(intext):

    return 


with open('inputs/12in.txt', 'r') as infile:
    tests = infile.read()


#tests = sample1
#print tests

print solve1(tests)
#print solve2(tests)
