sample1='''hijklmmn'''

def increment(password):
    incremented = list(password[::-1])
    done = False
    for i in range(len(incremented)):
        if not done:
            if incremented[i] != 'z':
                done = True
                incremented[i] = chr(ord(incremented[i])+1)
            else:
                incremented[i] = 'a'
    return incremented[::-1]

def increasing(password):
    for i in range(len(password)-2):
        if ord(password[i]) == ord(password[i+1])-1 and ord(password[i]) == ord(password[i+2])-2:
            return True
    return False

def banned(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    return True

def pairs(password):
    first = -1
    for i in range(len(password)-1):
        if password[i] == password[i+1] and i != first:
            if first == -1:
                first = i + 1
            else:
                return True
    return False

def solve1(intext):
    password = list(intext)
    done = increasing(password) and banned(password) and pairs(password)
    while not done:
        password = increment(password)
        done = increasing(password) and banned(password) and pairs(password)
        #print ''.join(password)
    return ''.join(password) 


with open('inputs/11in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests

a = solve1(tests)
print a
print solve1(increment(a))
