import re
import json

sample1=''''''

def solve1(intext):
    removed = re.findall('-?[0-9]\d*',intext)
    removed = map(int, removed)
    #print removed
    return sum(removed)

def parsejson(jsonin):
    # Get value if int
    if type(jsonin) == int:
        return jsonin
    # Ignore strings
    if type(jsonin) == unicode:
        return 0
    # Get value if array(list)
    if type(jsonin) == list:
        return sum([parsejson(subobject) for subobject in jsonin])
    # if object with red ignore else parse
    if type(jsonin) == dict:
        if 'red' in jsonin.values():
            return 0
        else:
            return parsejson(list(jsonin.values()))

def solve2(intext):
    jsonin = json.loads(intext)
    parsejson(jsonin)
    #print json.dumps(jsonin, sort_keys=True,indent=4, separators=(',', ': '))
    return parsejson(jsonin)


with open('inputs/12in.txt', 'r') as infile:
    tests = infile.read()


#tests = sample1
#print tests

print solve1(tests)
print solve2(tests)
