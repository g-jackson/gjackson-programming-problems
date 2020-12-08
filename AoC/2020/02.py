
def a(inputs):
    valid_count = 0
    for input in inputs:
        min_range = int(input.split()[0].split('-')[0])
        max_range = int(input.split()[0].split('-')[1])
        character = input.split()[1][:-1]
        password = input.split()[2]
        print(min_range, max_range, character, password, password.count(character))
        if (password.count(character) >= min_range and password.count(character) <= max_range):
            valid_count += 1

    return valid_count


def b(inputs):
    valid_count = 0
    for input in inputs:
        start_pos = int(input.split()[0].split('-')[0])
        end_pos = int(input.split()[0].split('-')[1])
        character = input.split()[1][:-1]
        password = input.split()[2]
        print(start_pos, end_pos, character, password, password.count(character))
        if (password[start_pos - 1] == character) ^ (password[end_pos - 1] == character):
            valid_count += 1
            print(True)

    return valid_count



with open('inputs/02in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
