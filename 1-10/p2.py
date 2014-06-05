import sys

#find if prime
def prime(x):
    for i in range (2,x-1):
        if x % i == 0:
            return False
    return True

#iterate range
def primes(min, max):
    #print "min %d, max %d" % (min, max)
    for i in range (min, max+1):
        if prime(i):
            print i
    print ""

#get input
def main():
    i = input()
    for x in range (0,i):
        line = sys.stdin.readline().split()
        max = (int)(line[1])
        min = (int)(line[0])
        primes(min,max)


main()
