def solve1(captcha):
    digits = list(captcha)
    total = 0
    current = 0
    prev = -1
    while current < len(digits):
        if digits[current] == digits[prev]:
            total += int(digits[current])
        print digits[prev], digits[current], total
        current+=1
        prev+=1
    return total

def solve2(captcha):
    digits = list(captcha)
    total = 0
    current = 0
    prev = -(len(digits)/2)
    while current < len(digits):
        if digits[current] == digits[prev]:
            total += int(digits[current])
        print digits[prev], digits[current], total
        current+=1
        prev+=1
    return total

captcha = '1212'
print captcha

print solve1(captcha)
print solve2(captcha)