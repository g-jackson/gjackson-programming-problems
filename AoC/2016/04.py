from collections import Counter
import re
sample1='''aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
qzmt-zixmtkozy-ivhz-343[test]'''



def solve1(intext):
    total = 0
    for line in intext:
        checksumsize = 5
        name = re.sub('-', '', line.split('[')[0][:-3])
        sector = (int)(line.split('[')[0][-3:])
        checksum = line.split('[')[1][0:checksumsize]
        counter = Counter(name)
        splitlist = counter.items()
        splitlist = sorted(splitlist, key = lambda element : element[0])
        splitlist = sorted(splitlist, key = lambda element : element[1], reverse=True)
        #print splitlist
        gensum = []
        for i in range(checksumsize):
            gensum.append(splitlist[i][0])
        gensum = ''.join(gensum)
        if gensum == checksum:
            total = total + sector
        #print name, sector, counter, checksum, 
    return total

def solve2(intext):
    result = ''
    for line in intext:
        checksumsize = 5
        name = line.split('[')[0][:-3]
        sector = (int)(line.split('[')[0][-3:])
        checksum = line.split('[')[1][0:checksumsize]
        rotations = sector % 26
        decrypted = []
        for char in name:
            newchar = ''
            if char != '-':
                newchar = ord(char) + rotations
                if newchar > 122:
                    newchar = newchar - 26
                newchar = chr(newchar)
            else:
                newchar = ' '
            decrypted.append(newchar)
        print name, ''.join(decrypted), rotations
        if ''.join(decrypted) == "northpole object storage ":
            result = sector
    return result


with open('inputs/04in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')

#print tests

#print solve1(tests)
print solve2(tests)
