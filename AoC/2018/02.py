#testinputs = ["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]
testinputs = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

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
        print(input, addtwo, addthree, sumtwo, sumthree)
    return sumtwo * sumthree


def count_letters(word, char):
    char = chr(97+char)
    return sum(char == c for c in word)


def b(inputs):
    for input in inputs:
        for match in inputs:
            comparison = zip(input, match)
            count = 0
            for char in comparison:
                if char[0] == char[1]:
                    count += 1
            if count == len(input) - 1:
                result = ""
                for char in comparison:
                    if char[0] == char[1]:
                        result += char[0]
                return result


with open('inputs/02in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split()

#print(a(inputs))
print(b(inputs))
