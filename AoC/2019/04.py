testinputs = 111111
testinputs = 223450
testinputs = 123789


def is_valid_password_a(input):
    valid = True
    # Is six digits
    if len(str(input)) != 6:
        valid = False

    # Has two adjacent matching digits
    matching = False
    prev = input % 10
    for i in range(5):
        next = input // 10**(i+1) % 10
        #print(prev, next)
        if prev == next:
            matching = True
        if prev < next:
            valid = False
        prev = next
    if not matching:
        valid = False
    return valid


def a(min, max):
    total = 0
    for i in range(min, max + 1):
        if is_valid_password_a(i):
            total += 1
    return total


def is_valid_password_b(input):
    valid = True
    # Is six digits
    if len(str(input)) != 6:
        valid = False

    # Has two adjacent matching digits
    matching = False
    match_count = 0
    prev = input % 10
    for i in range(5):
        next = input // 10**(i+1) % 10
        #print(prev, next)
        if prev == next:
            match_count += 1
        else:
            if match_count == 1:
                matching = True
            match_count = 0
        if prev < next:
            valid = False
        prev = next
    if match_count == 1:
        matching = True
    if not matching:
        valid = False
    return valid


def b(min, max):
    total = 0
    for i in range(min, max + 1):
        if is_valid_password_b(i):
            total += 1
    return total


min = 236491
max = 713787

print(is_valid_password_a(111111), is_valid_password_a(223450), is_valid_password_a(123789))
print(is_valid_password_b(112233), is_valid_password_b(123444), is_valid_password_b(111122))

print(a(min, max))
print(b(min, max))
#print tests
