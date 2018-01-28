sample1='''111100001010'''

def generatecurve(initial, endlength):
    outstring = initial
    while len(outstring) < endlength:
        forward = (str)(outstring)
        forward = forward[2:]
        backward = initial[:1:-1]
        backward = backward.replace("0", "2")
        backward = backward.replace("1", "0")
        backward = backward.replace("2", "1")
        outstring = forward + "0" + backward
    print outstring

def solve1(intext):
    length = 15#272
    initial = bin(int(intext, 2))
    #print initial
    generatecurve(initial, length)
    return 

def solve2(intext):

    return 


with open('inputs/16in.txt', 'r') as infile:
    tests = infile.read()

tests = sample1

print solve1(tests)
#print solve2(tests)
