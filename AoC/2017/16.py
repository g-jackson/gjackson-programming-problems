sample1 ='''s1,x3/4,pe/b'''


def solve1(inlist):
    order = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
    #print order
    for move in inlist:
        print move
        if move[0] == 's':
            spin = len(order) - (int)(move[1:])
            order = order[spin:]+order[:spin]
        elif move[0] == 'x':
            pos1 = (int)(move.split('/')[0][1:])
            val1 = order[pos1]
            pos2 = (int)(move.split('/')[1])
            val2 = order[pos2]
            order[pos1] = val2
            order[pos2] = val1
        elif move[0] == 'p':
            val1 = move[1]
            pos1 = order.index(val1)
            val2 = move[3]
            pos2 = order.index(val2)
            order[pos2] = val1
            order[pos1] = val2
        print order

            
    outstring = ''
    for char in order:
        outstring = outstring + char
    return outstring

def solve2(inlist):

    return



with open('16in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split(',')

#print test
#print solve1(test)
print solve2(test)

