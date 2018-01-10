def outer_range(number):
    i = 1
    while number > (i)*(i):
        i = i+2
    return i

def cardinals(layer):
    center1 = (layer*layer)-(layer/2)
    center2 = center1 - layer + 1
    center3 = center2 - layer + 1 
    center4 = center3 - layer + 1
    return center1, center2, center3, center4

def distance_to_card(cards, number):
    distance = number
    for card in cards:
        if abs(card - number)< distance:
            distance = abs(card - number)
    print "distance", distance
    return distance

def solve(number):
    print number
    layer = outer_range(number)
    print layer
    cards = cardinals(layer)
    print cards
    result = distance_to_card(cards, number) + (layer/2)
    return result

def solve1(number):
    anticlockwise = [(1,0),(0,1),(-1,0),(0,-1)]
    coords = {(0,0):1}
    pos = (0,0)
    counter = 1
    direction = 0
    left = 1

    while counter < number:
        counter = counter + 1
        newpos = (pos[0]+anticlockwise[direction][0], pos[1]+anticlockwise[direction][1])

        #print "pos", pos, "newpos", newpos, "direction", anticlockwise[direction]
        pos = newpos
        leftcoord = (pos[0]+anticlockwise[left][0], pos[1]+anticlockwise[left][1])
        #print leftcoord
        #print coords
        coords[pos] = counter
        if leftcoord not in coords:
            #print "no left, changing direction"
            if left < 3:
                left = left + 1
            else:
                left = 0
            if direction < 3:
                direction = direction + 1
            else:
                direction = 0     

    print pos
    return abs(pos[0]) + abs(pos[1])

def solve2(number):
    anticlockwise = [(1,0),(0,1),(-1,0),(0,-1)]
    coords = {(0,0):1}
    pos = (0,0)
    high = 0
    direction = 0
    left = 1
    while high < number:
        newvalue = 0
        
        # Get prev and prev left coords to calculate new value
        prev = pos
        prevleft = pos[0]+anticlockwise[left][0], pos[1]+anticlockwise[left][1]
        
        # Move pos
        newpos = (pos[0]+anticlockwise[direction][0], pos[1]+anticlockwise[direction][1])
        pos = newpos

        # Get left and next left coords to calculate new value
        leftcoord = (pos[0]+anticlockwise[left][0], pos[1]+anticlockwise[left][1])
        nextleft = (pos[0]+anticlockwise[left][0]+anticlockwise[direction][0], pos[1]+anticlockwise[left][1]+anticlockwise[direction][1])

        # Calculate new value
        if prev in coords:
            newvalue = newvalue + coords[prev]
            #print prev, coords[prev]
        if prevleft in coords:
            newvalue = newvalue + coords[prevleft]
            #print prevleft, coords[prevleft]
        if leftcoord in coords:
            newvalue = newvalue + coords[leftcoord]
            #print leftcoord, coords[leftcoord]
        if nextleft in coords:
            newvalue = newvalue + coords[nextleft]
            #print nextleft, coords[nextleft]
        print newvalue
        high = newvalue

        coords[pos] = newvalue
        #print coords

        # If nothing to left turn left
        if leftcoord not in coords:
            if left < 3:
                left = left + 1
            else:
                left = 0
            if direction < 3:
                direction = direction + 1
            else:
                direction = 0     

    print pos
    return high

number = 325489
#number = 809
#print solve(number)
#print solve1(number)
print solve2(number)
# layer of spiral
