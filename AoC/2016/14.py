import hashlib
import re
sample1='''abc'''

def solve1(intext):
    keys = []
    counter = 0
    result = 0
    while len(keys) < 64:
        hashing = intext + (str)(counter)
        hashed = hashlib.md5(hashing).hexdigest()
        recheck = re.compile('(.)\\1{2}').search(hashed)
        if recheck:
            #print hashing
            valid = False
            findchar = recheck.group(0)[0]
            for i in range(1000):

                subhashing = intext + (str)(counter+i+1)
                subhashed = hashlib.md5(subhashing).hexdigest()
                subrecheck = re.compile(r'%s{5}'%findchar).search(subhashed)
                if subrecheck and not valid:
                    print len(keys), findchar, hashing, hashed, subhashing, subhashed
                    result = counter
                    valid = True
            if valid:
                keys.append(hashed)

        counter = counter + 1
    return result

def solve2(intext):

    return 


with open('inputs/14in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests

print solve1(tests)
#print solve2(tests)
