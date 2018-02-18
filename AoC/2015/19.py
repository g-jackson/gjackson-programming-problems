import re
sample1='''H => HO
H => OH
O => HH

HOHOHO'''
def solve1(intext):
    startstring = intext[-1]
    replacements = intext[0:-2]
    replace = {}
    for replacement in replacements:
        fromstring = replacement.split(' => ')[0]
        tostring = replacement.split(' => ')[1]
        if fromstring not in replace:
            replace[fromstring] = [tostring]
        else:
            replace[fromstring].append(tostring)
    print replace
    newmolecules = []
    for r in replace:
        starts = [match.start() for match in re.finditer(re.escape(r), startstring)]
        matches = replace[r]
        for match in matches:
            for start in starts:
                newmolecule = "".join([startstring[0:start] , match , startstring[start+len(r):]])
                #print "found", r, "=>", match, "start:", start, "newmolecule:", newmolecule
                #print startstring[0:start] , match , startstring[start+1:]
                if newmolecule not in newmolecules:
                    newmolecules.append(newmolecule)
    return len(newmolecules)

#615

def solve2(intext):

    return 


with open('inputs/19in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
print solve1(tests)
#print solve2(tests)
