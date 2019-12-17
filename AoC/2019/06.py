import sys
sys.setrecursionlimit(10000)

testinputs = []
testinputs = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
testinputs = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]


class Tree:
    value = ""
    leaves = []
    distance_from_com = 0
    parent = None

    def __init__(self, value, distance_from_com, orbits, parent=None):
        self.value = value
        self.parent = parent
        self.distance_from_com = distance_from_com
        self.leaves = []
        if value in orbits:
            leaves = orbits[value]
            for leaf in leaves:
                #print("adding", leaf, "to", self.value, "distance", distance_from_com + 1)
                self.leaves.append(Tree(leaf, distance_from_com + 1, orbits, self))
               

    def sum_sub_orbits(self):
        sum = 0
        #print("summing", self.value, self.leaves)
        if self.leaves != []:
            for leaf in self.leaves:
                sum += leaf.sum_sub_orbits()
            return sum + self.distance_from_com
        else:    
            return self.distance_from_com
    
    def get_leaf(self, value):
        for leaf in self.leaves:
            if leaf.value == value:
                return leaf
            else:    
                found = leaf.get_leaf(value)
                if found:
                    return found

    def list_parents(self):
        output = []
        leaf = self.parent
        while leaf.parent != None:
            output.append(leaf.value)
            leaf = leaf.parent
        output.append("COM")
        return output


def a(inputs):
    inputs = inputs.copy()
    # Organize inputs into dict
    for i in range(len(inputs)):
        inputs[i] = inputs[i].split(")")
    orbits = {}
    for input in inputs:
        if input[0] in orbits:
            orbits[input[0]].append(input[1])
        else:
            orbits[input[0]] = [input[1]]
    
    #print(orbits)
    tree = Tree("COM", 0, orbits)
    return tree.sum_sub_orbits()



def b(inputs):
    # Organize inputs into dict
    inputs = inputs.copy()
    for i in range(len(inputs)):
        inputs[i] = inputs[i].split(")")
    orbits = {}
    for input in inputs:
        if input[0] in orbits:
            orbits[input[0]].append(input[1])
        else:
            orbits[input[0]] = [input[1]]
    
    #print(orbits)
    tree = Tree("COM", 0, orbits)
    you_pos = tree.get_leaf("YOU")
    san_pos = tree.get_leaf("SAN")
    you_orbits = (you_pos.list_parents())
    san_orbits = (san_pos.list_parents())
    #print(you_orbits, san_orbits)
    for i in you_orbits:
        if i in san_orbits:
            first_match = i
            break

    return you_orbits.index(first_match) + san_orbits.index(first_match)


with open('inputs/06in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split()




#print(inputs)
#print(a(testinputs))
print(a(inputs))
#print(b(testinputs))
print(b(inputs))

#print tests
