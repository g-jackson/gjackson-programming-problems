testinputs = "dabAcCaCBAcCcaDA"
import string

def a(input):
    i = 0
    while i < len(input):
        input, i = match(input, i)
        i+=1 
    #print(input)
    return len(input)

def b(input):
    min = "a"
    min_score = len(input)
    for i in string.ascii_lowercase:
        poly_string = input
        poly_string = poly_string.replace(i, "")
        poly_string = poly_string.replace(i.upper(), "")
        score = a(poly_string)
        if score < min_score:
            min_score = score
            min = i
        print(i, score, min, min_score)
    return min_score


def match(input, i):
    #print(i)
    if (i < 0) or (i >= len(input) - 1):
        return input, i
    if (((input[i].isupper() and input[i + 1].islower()) or 
        (input[i].islower() and input[i + 1].isupper())) and
        input[i].upper() == input[i + 1].upper()
        ):
            #print("match at :", i, input[i], input[i + 1])
            input = input[:i] + input[i+2:]
            input, i = match(input, i - 1)
    return input, i

with open('inputs/05in.txt', 'r') as infile:
    input = infile.read()


print(a(input))
print(b(input))
