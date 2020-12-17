
def a(inputs):
    total = 0
    bags = {}
    for bag in inputs:
        print(bag)
        name = ''.join(bag.split(' ')[0:2])
        contents = ''.join(bag.split('contain')[1]).split(',')
        contains = []
        for content in contents:
            if "no other bags." not in content:
                content = content.strip().split()
                number = content[0]
                colour = ''.join(content[1:3])
                contains.append((number, colour))
        print(contains)
        bags[name] = contains
    print(bags)
    return total


def b(inputs):
    total = 0
    return total


with open('inputs/07in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
