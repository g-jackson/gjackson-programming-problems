sample1 ='''{}
{{{}}}
{{},{}}
{{{},{},{{}}}}
{<{},{},{{}}>}
{<a>,<a>,<a>,<a>}
{{<a>},{<a>},{<a>},{<a>}}
{{<!>},{<!>},{<!>},{<a>}}'''

def endgroup(string,points):
    #print "finding end of group in ", string
    score = points
    skipchar = False
    charpos = 0
    groups = 1
    endchar = -1
    garbage = 0
    while endchar == -1:
        if skipchar:
            skipchar = False
        else:
            char = string[charpos]
            if char == '!':
                skipchar = True
            if char == '<':
                end, removedgarbage = endgarbage(string[charpos+1:])
                charpos = charpos + end + 1
                garbage = garbage + removedgarbage
            if char == '{':
                subpoints, subgroups, removedgarbage, end =  endgroup(string[charpos+1:], points+1)
                charpos = charpos + end + 1
                groups = groups + subgroups
                score = score + subpoints
                garbage = garbage + removedgarbage
            if char == '}':
                endchar = charpos
        charpos = charpos + 1

    return score, groups, garbage, endchar

def endgarbage(string):
    #print "finding end of garbage in ", string
    endchar = -1
    skipchar = False
    charpos = 0
    garbage = 0
    while endchar == -1:
        if skipchar:
            skipchar = False
        else:
            char = string[charpos]
            if char == '!':
                skipchar = True
            elif char == '>':
                endchar = charpos
            else:
                garbage = garbage + 1
        charpos = charpos + 1
    return endchar, garbage

def solve1(inlist):
    groups = 0
    for line in inlist:
        results = endgroup(line[1:],1)
        print line
        print "points",  results[0], "groups", results[1], "garbage", results[2]
    return results[0]

def solve2(inlist):
    return


with open('inputs/09in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')


#print test
print solve1(test)

#print solve2(test)

