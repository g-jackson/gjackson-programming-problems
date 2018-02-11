from itertools import combinations_with_replacement
from collections import Counter
sample1='''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''

def readinput(intext):
    ingredients = []
    for line in intext:
        split = line.split()
        name = split[0][:-1]
        capacity = (int)(split[2][:-1])
        durability = (int)(split[4][:-1])
        flavor = (int)(split[6][:-1])
        texture = (int)(split[8][:-1])
        calories = (int)(split[10])
        ingredients.append((capacity, durability, flavor, texture, calories))
        #ingredients[name] = (capacity, durability, flavor, texture, calories)
    return ingredients

def getscore(ingredients, split, calories):
    totalprop = [0,0,0,0,0]
    for ingredient in split:
        properties = ingredients[ingredient]
        for prop in range(len(properties)):
            totalprop[prop] += properties[prop]*split[ingredient]
    #print split, properties, totalprop
    score = 0
    if totalprop[-1] == calories or calories == 0:
        score = 1
        for i in totalprop[:-1]:
            if i > 0:
                score *=i
    return score


def solve1(intext):
    ingredients = readinput(intext)
    maxscore = 0
    for combo in combinations_with_replacement(range(len(ingredients)),100):
        counts = Counter(combo)
        score = getscore(ingredients, counts, 0)
        if score > maxscore:
            maxscore = score
    return maxscore

def solve2(intext):
    ingredients = readinput(intext)
    print ingredients[0]
    maxscore = 0
    for combo in combinations_with_replacement(range(len(ingredients)),100):
        counts = Counter(combo)
        score = getscore(ingredients, counts, 500)
        if score > maxscore:
            maxscore = score
    return maxscore


with open('inputs/15in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests
tests = tests.split('\n')

print solve1(tests)
print solve2(tests)
