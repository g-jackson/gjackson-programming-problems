testinputs = ["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]

def a(inputs):
    sumtwo = 0
    sumthree = 0
    for input in inputs:
        addtwo = False
        addthree = False
        for char in range(0,26):
            if count_letters(input, char) == 2:
                addtwo = True
            if count_letters(input, char) == 3:
                addthree = True
        if addtwo:
            sumtwo += 1
        if addthree:
            sumthree += 1
        print input, addtwo, addthree, sumtwo, sumthree
    return sumtwo * sumthree


def count_letters(word, char):
    char = chr(97+char)
    return sum(char == c for c in word)


def b(inputs):
    return



with open('inputs/02in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split()
print inputs

#print a(inputs)
print b(inputs)
