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

number = 325489
print solve(1)
print solve(12)
print solve(23)
print solve(1024)
print solve(number)
# layer of spiral
