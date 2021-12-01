test_inputs = '''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''.split('\n')


def match(message, rule_dict):
    # Iterate over rules, take each path with down ORs until they output wrong char then backtrack.
    # Alternatively generate all possible strings given the rule set, probably computationally too heavy.

    return True


def a(inputs):
    split = inputs.index('')
    rules = inputs[0:split]
    messages = inputs[split:-1]
    # print(rules, messages)
    rule_dict = {}
    for rule in rules:
        line = rule.split(' ')
        if '|' in line:
            instruction = [[line[1], line[2]], [line[3], line[4]]]
            rule_dict[line[0]] = instruction
        elif len(line) == 2 and ('\"' in line[2]):
            rule_dict[line[0]] = line[1].strip('\"')
        else:
            pass
    total_matches = 0
    print(rule_dict)
    for message in messages:
        if match(message, rule_dict):
            total_matches += 1
    return total_matches


def b(inputs):
    return


with open('inputs/18in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(test_inputs))
print(b(inputs))
