sample1='''10000'''

def gencurve(initial, endlength):
    outstring = initial
    while len(outstring) <= endlength:
        forward = outstring
        backward = forward[::-1]
        backward = backward.replace("0", "2")
        backward = backward.replace("1", "0")
        backward = backward.replace("2", "1")
        outstring = forward + "0" + backward
        #print "fw", forward, "bw", backward, "total", outstring, "len", len(outstring)
    return outstring[:endlength]

def genchecksum(inputstring):
    checksum = inputstring
    while len(checksum) % 2 == 0:
        newchecksum = ""
        for i in range(len(checksum)/2):
            if checksum[i*2] == checksum[(i*2)+1]:
                newchecksum += "1"
            else:
                newchecksum += "0"
        checksum = newchecksum
        #print len(newchecksum), newchecksum
    return checksum

def solve1(intext):
    length = 35651584
    #print initial
    generated = gencurve(intext, length)
    #print "gen", generated
    checksum = genchecksum(generated)
    return checksum

def solve2(intext):

    return 


with open('inputs/16in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1

print solve1(tests)
#print solve2(tests)
