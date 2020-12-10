test_input = '''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''


def a(inputs):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_count = 0
    for input in inputs:
        fields = input.split()
        keys_present = []
        for field in fields:
            keys_present.append(field.split(':')[0])
        valid = True
        for key in required:
            if key not in keys_present:
                valid = False
        if valid:
            valid_count += 1
        print(keys_present, valid)
    return valid_count


def validate(fields):
    valid = True
    for field in fields:
        key, value = field.split(':')
        valid_key = False
        if key == 'byr':
            if len(value) == 4 and value.isdigit() and int(value) >= 1920 and int(value) <= 2002:
                valid_key = True
        if key == 'iyr':
            if len(value) == 4 and value.isdigit() and int(value) >= 2010 and int(value) <= 2020:
                valid_key = True
        if key == 'eyr':
            if len(value) == 4 and value.isdigit() and int(value) >= 2020 and int(value) <= 2030:
                valid_key = True
        if key == 'hgt':
            if value[-2:] == 'cm' and int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                valid_key = True
            elif value[-2:] == 'in' and int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                valid_key = True
        if key == 'hcl':
            if value[0] == '#' and [i for i in value[1:] if i.isdigit() or i in ['a', 'b', 'c', 'd', 'e']] and len(value) == 7:
                valid_key = True
        if key == 'ecl':
            if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid_key = True
        if key == 'pid':
            if value.isdigit() and len(value) == 9:
                valid_key = True
        if key == 'cid':
            valid_key = True
        print(key, value, valid_key)
        if not valid_key:
            valid = False
    return valid


def b(inputs):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_count = 0
    for entry in inputs:
        fields = entry.split()
        keys_present = []
        for field in fields:
            keys_present.append(field.split(':')[0])
        valid = True
        for key in required:
            if key not in keys_present:
                valid = False
        if valid and validate(fields):
            valid_count += 1
        print(fields, valid)
    return valid_count


with open('inputs/04in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n\n')
# nputs = test_input.split('\n\n')

print(a(inputs))
print(b(inputs))
