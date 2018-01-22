sample1='''..^^.'''
sample2='''.^^.^.^^^^'''

def istrap(l,m,r):
    trap = False
    if l == "^" and m == "^" and r == ".":
        trap = True
    if l == "." and m == "^" and r == "^":
        trap = True
    if l == "^" and m == "." and r == ".":
        trap = True
    if l == "." and m == "." and r == "^":
        trap = True
    return trap

def solve1(intext):
    genrows = 40
    rows = [list(intext)]
    print rows
    for row in range(genrows-1):
        rows.append([])
        newrow = rows[row+1]
        oldrow = rows[row]
        for char in range(len(rows[row])):
            l = 0
            m = 0
            r = 0
            if char == 0:
                l = '.'
                m = rows[row][char]
                r = rows[row][char+1]
            elif char == len(rows[row])-1:
                l = rows[row][char-1]
                m = rows[row][char]
                r = '.'
            else:
                l = rows[row][char-1]
                m = rows[row][char]
                r = rows[row][char+1]
            print l, m, r
            if istrap(l,m,r):
                print "trap"
                newrow.append('^')
            else:
                print "not trap"
                newrow.append('.')

    total = 0
    for row in rows:
        print ''.join(row)
        total = total + row.count(".")
    return total

def solve2(intext):
    genrows = 400000
    rows = [list(intext)]
    #print rows
    for row in range(genrows-1):
        rows.append([])
        newrow = rows[row+1]
        oldrow = rows[row]
        for char in range(len(rows[row])):
            l = 0
            m = 0
            r = 0
            if char == 0:
                l = '.'
                m = rows[row][char]
                r = rows[row][char+1]
            elif char == len(rows[row])-1:
                l = rows[row][char-1]
                m = rows[row][char]
                r = '.'
            else:
                l = rows[row][char-1]
                m = rows[row][char]
                r = rows[row][char+1]
            #print l, m, r
            if istrap(l,m,r):
                #print "trap"
                newrow.append('^')
            else:
                #print "not trap"
                newrow.append('.')
        # for matchrow in range(len(rows)-1):
        #     if newrow == rows[matchrow]:
        #         print matchrow
    total = 0
    for row in rows:
        #print ''.join(row)
        total = total + row.count(".")
    return total


with open('inputs/18in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample2
#print tests

#print solve1(tests)
print solve2(tests)
