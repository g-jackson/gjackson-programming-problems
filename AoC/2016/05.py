import hashlib
sample1='''abc'''
def solve1(intext):
    password = ""
    counter = 0
    while len(password) < 8:
        hashing = intext + (str)(counter)
        hashed = hashlib.md5(hashing).hexdigest()
        if hashed[:5] == "00000":
            print hashed
            password += hashed[5]
        counter = counter + 1
    return password

def solve2(intext):
    password = ['-','-','-','-','-','-','-','-']
    counter = 0
    resolved = 0
    while resolved < 8:
        hashing = intext + (str)(counter)
        hashed = hashlib.md5(hashing).hexdigest()
        if hashed[:5] == "00000":
            pos = hashed[5]
            if not pos.isalpha():
                pos = (int)(pos)
                if pos < 8:
                    if password[pos] == '-':
                        password[pos] = hashed[6]
                        resolved = resolved + 1
            print hashed, ''.join(password), hashing

        counter = counter + 1
    return ''.join(password)


with open('inputs/05in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
print tests

#print solve1(tests)
print solve2(tests)
