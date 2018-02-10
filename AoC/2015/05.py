from collections import Counter
sample1='''ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb
qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy'''

def vowels(i):
    counts = Counter(i)
    if counts['a'] + counts['e'] + counts['i'] + counts['o'] + counts['u'] > 2:
        return True
    return False

def doubles(i):
    valid = False
    for letter in range(len(i)-1):
        if i[letter] == i[letter+1]:
            valid = True
    return valid

def banned(i):
    if "ab" in i or "cd" in i or "pq" in i or "xy" in i:
        return False
    return True


def solve1(intext):
    counter = 0
    for i in intext:
        valid = vowels(i) and doubles(i) and banned(i)
        if valid:
            print "nice", i
            counter += 1
        else:
            print "naughty", i
    return counter

def repeatpattern(i):
    for letter in range(len(i)-1):
        pattern = i[letter] + i[letter+1]
        for match in range(len(i)-1):
            if match != letter and match + 1 != letter and match - 1 != letter:
                if i[match] + i[match+1] == pattern:
                    print i[match] + i[match+1], match, letter,
                    return True

    return False

def repeatletter(i):
    for letter in range(len(i)-2):
        if i[letter] == i[letter+2]:
            return True
    return False

def solve2(intext):
    counter = 0
    for i in intext:
        valid = repeatpattern(i) and repeatletter(i)
        if valid:
            print "nice", i
            counter += 1
        else:
            print "naughty", i
    return counter


with open('inputs/05in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')
#print solve1(tests)
print solve2(tests)
