def a(inputs):
    total = 0
    for bag in inputs:
        # Split bag
        bag_list = [*bag]
        c1 = bag_list[len(bag_list)//2:]
        c2 = bag_list[:len(bag_list)//2]

        # Find match
        shared = ''
        for item in c1:
            if item in c2:
                shared = item

        # Score values
        is_upper = shared.isupper()
        shared = shared.lower()
        score = (is_upper * 26) + ord(shared) - 96
        total += score
        # print(shared, ord(shared), is_upper, score)
    return total

def b(inputs):
    total = 0
    for i in range(len(inputs) // 3):
        # Create groups
        b1, b2, b3 = inputs[i*3 : (i*3) + 3]

        # Find match
        shared = ''
        for item in b1:
            if item in b2 and item in b3:
                shared = item

        # Score values
        is_upper = shared.isupper()
        shared = shared.lower()
        score = (is_upper * 26) + ord(shared) - 96
        total += score
        # print(shared, ord(shared), is_upper, score)
    return total

input_file = 'inputs/03test.txt'
input_file = 'inputs/03in.txt'

with open(input_file, 'r') as infile:
    inputs = infile.read()

inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
