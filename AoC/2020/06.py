
def a(inputs):
    total = 0
    for group in inputs:
        answers = [False] * 26
        group = group.split('\n')
        # print(group)
        for person in group:
            for answer in person:
                answers[ord(answer) - 97] = True
            # print(person)
        # print(answers)
        total += answers.count(True)
    return total


def b(inputs):
    total = 0
    for group in inputs:
        answers = [0] * 26
        group = group.split('\n')
        # print(group)
        for person in group:
            for answer in person:
                answers[ord(answer) - 97] += 1
            # print(person)
        # print(answers)
        total += answers.count(len(group))
    return total


with open('inputs/06in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n\n')

print(a(inputs))
print(b(inputs))
