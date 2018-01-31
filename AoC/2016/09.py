sample1='''ADVENT
A(1x5)BC
(3x3)XYZ
A(2x2)BCD(2x2)EFG
(6x1)(1x3)A
X(8x2)(3x3)ABCY
(3x3)XYZ
X(8x2)(3x3)ABCY
(27x12)(20x12)(13x14)(7x10)(1x12)A
(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'''

def solve1(intext):
    genstring = ''
    for line in intext:
        genstring = ''
        counter = 0
        while counter < len(line):
            if line[counter] != '(':
                genstring += line[counter]
            else:
                #print line[counter:], line[counter:].find(')')
                end = line[counter:].find(')')
                repetition = line[counter+1:counter+end].split('x')
                repetition = [(int)(repetition[0]), (int)(repetition[1])]
                #print repetition
                for i in range(repetition[1]):
                    genstring += line[counter+end+1:counter+end+1+repetition[0]]
                counter = counter + end + repetition[0]
            counter = counter + 1
        print len(genstring), genstring
    return len(genstring)

def decompress(line):
    #print line
    length = 0
    counter = 0
    while counter < len(line):
        if line[counter] != '(':
            length += 1
        else:
            #print line[counter:], line[counter:].find(')')
            end = line[counter:].find(')')
            repetition = line[counter+1:counter+end].split('x')
            repetition = [(int)(repetition[0]), (int)(repetition[1])]
            #print repetition
            decompressed = decompress(line[counter+end+1:counter+end+1+repetition[0]])
            for i in range(repetition[1]):
                length += decompressed
            counter = counter + end + repetition[0]
        counter = counter + 1
    return length

def solve2(intext):
    for line in intext:
        length = decompress(line)
        print length
    #return len(genstring)


with open('inputs/09in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')
print tests

#print solve1(tests)
print solve2(tests)
