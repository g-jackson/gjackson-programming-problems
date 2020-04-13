testinputs = [
    "9 players; last marble is worth 25 points",
    "10 players; last marble is worth 1618 points",
    "13 players; last marble is worth 7999 points",
    "17 players; last marble is worth 1104 points",
    "21 players; last marble is worth 6111 points",
    "30 players; last marble is worth 5807 points"
]

def a(input):
    players = int(input.split(" ")[0])
    points = int(input.split(" ")[6])
    scores = [0]*players
    circle = [0]
    current_player = 0
    current_marble_index = 0 
    print(players, points)
    for new_marble in range(1, points + 1):
        #print("[", current_player, "]", "-", current_marble_index, "->", circle[current_marble_index], "-", circle)
        if new_marble % 23 != 0:
            current_marble_index += 2
            if current_marble_index > len(circle):
                current_marble_index = 1
            circle.insert(current_marble_index, new_marble)
        else:
            scores[current_player] += new_marble
            current_marble_index -= 7
            if current_marble_index < 0:
                current_marble_index = len(circle) + current_marble_index
                print("here", circle[current_marble_index], current_player)
            scores[current_player] += circle.pop(current_marble_index)
        current_player = (current_player + 1) % players

    print(scores)
    return max(scores)


def b(input):
    players = int(input.split(" ")[0])
    points = int(input.split(" ")[6]) * 100
    scores = [0]*players
    circle = [0]
    current_player = 0
    current_marble_index = 0 
    print(players, points)
    for new_marble in range(1, points + 1):
        #print("[", current_player, "]", "-", current_marble_index, "->", circle[current_marble_index], "-", circle)
        if new_marble % 100000 == 0:
            print(new_marble)
        if new_marble % 23 != 0:
            current_marble_index += 2
            if current_marble_index > len(circle):
                current_marble_index = 1
            circle.insert(current_marble_index, new_marble)
        else:
            scores[current_player] += new_marble
            current_marble_index -= 7
            if current_marble_index < 0:
                current_marble_index = len(circle) + current_marble_index
            scores[current_player] += circle.pop(current_marble_index)
        current_player = (current_player + 1) % players

    print(scores)
    return max(scores)


with open('inputs/09in.txt', 'r') as infile:
    inputs = infile.read()
inputs = [inputs]


print(a(inputs[0]))
#print(a(testinputs[2]))

print(b(inputs[0]))
