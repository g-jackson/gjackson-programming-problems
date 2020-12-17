test_inputs = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''
test_inputs2 = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''


def a(inputs):
    bags = {}
    for bag in inputs:
        name = ''.join(bag.split(' ')[0:2])
        contents = ''.join(bag.split('contain')[1]).split(',')
        contains = []
        for content in contents:
            if "no other bags." not in content:
                content = content.strip().split()
                number = content[0]
                colour = ''.join(content[1:3])
                contains.append((number, colour))
        bags[name] = contains

    contains_gold = ['shinygold']
    done = False
    new_gold = []
    while not done:
        done = True
        for bag in bags:
            contents = bags[bag]
            for content in contents:
                if content[1] in contains_gold:
                    new_gold.append(bag)
                    #print(bag)
                    done = False
        for colour in new_gold:
            if colour not in contains_gold:
                contains_gold.append(colour)
        for colour in contains_gold:
            # print(bags[colour])
            if colour in bags:
                #print('removing', colour)
                del bags[colour]
    return len(contains_gold) - 1


def b(inputs):
    bags = {}
    for bag in inputs:
        name = ''.join(bag.split(' ')[0:2])
        contents = ''.join(bag.split('contain')[1]).split(',')
        contains = []
        for content in contents:
            if "no other bags." not in content:
                content = content.strip().split()
                number = int(content[0])
                colour = ''.join(content[1:3])
                contains.append((number, colour))
        bags[name] = contains

    total = get_count('shinygold', bags) - 1
    return total


def get_count(contents, bags):
    sum = 0
    if not bags[contents]:
        return 1
    for content in bags[contents]:
        sum += get_count(content[1], bags) * content[0]
        # print(contents, content, sum)
    return sum + 1


with open('inputs/07in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
