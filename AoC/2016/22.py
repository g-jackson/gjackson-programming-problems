sample1=''''''

def readinput(intext):
    disks = {}
    for line in intext:
        x = (int)((line.split()[0]).split('-')[1][1:])
        y = (int)((line.split()[0]).split('-')[2][1:])
        size = (int)(line.split()[2][:-1])
        used = (int)(line.split()[3][:-1])
        disks[(x,y)] = [size, used]
    #print disks
    return disks

def solve1(intext):
    disks = readinput(intext)
    total = 0
    for idisk in disks:
        data = disks[idisk][0]
        for jdisk in disks:
            if idisk != jdisk and data <= disks[jdisk][1] - disks[jdisk][0]:
                print idisk, "data fits on", jdisk , "it has", data, "and there is avail", disks[jdisk][1] - disks[jdisk][0]
                total = total + 1
    return total

def solve2(intext):

    return 


with open('inputs/22in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests
tests = tests.split('\n')

print solve1(tests)
#print solve2(tests)
