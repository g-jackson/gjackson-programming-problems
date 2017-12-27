import sys
for x in range (24):
    line = sys.stdin.readline().split()
    x = line[0]
    y = line[1]
    if y in x:
        print 1
    else:
        print 0
