import re
sample1='''abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn
ioxxoj[asdfgh]zxcvbnioxxoj[asdfgh]zxcvbn
aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb'''

def isabba(string):
    abba = False
    for i in range(len(string)-3):
        substring = string[i:i+4]
        if substring[0] == substring[3] and substring[1] == substring[2] and substring[0] != substring[1]:
            abba = True
            #print substring
    return abba

def getabas(string):
    abas = []
    for i in range(len(string)-2):
        substring = string[i:i+3]
        if substring[0] == substring[2]:
            abas.append(substring)
            #print substring
    return abas


def solve1(intext):
    total = 0
    for line in intext:
        valid = 0
        line = re.split('\]|\[',line)
        for i in range(len(line)):
            if valid == 0 and i % 2 == 0 and isabba(line[i]):
                valid = 1
            if i % 2 == 1 and isabba(line[i]):
                valid = 2
        if valid == 1:
            total = total + 1
        print valid, line 
    return total

def solve2(intext):
    total = 0
    for line in intext:
        valid = False
        line = re.split('\]|\[',line)
        abas = []
        for i in range(len(line)/2+1):
            abas = abas + getabas(line[i*2])

        for pattern in abas:
            bab = ''.join([pattern[1],pattern[0],pattern[1]])
            for i in range(len(line)/2):
                if bab in line[(i*2)+1]:
                    #print "match", pattern, line[(i*2)+1]
                    valid = True
        #print abas
        if valid:
            total = total + 1
        print valid, line 
    return total


with open('inputs/07in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')

#print solve1(tests)
print solve2(tests)
