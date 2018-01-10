sample1 ='''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''


def solve1(inlist):
    programs = {}
    for link in inlist:
        link = link.replace(",", "")
        link = link.split(" ")
        prog = link[0]
        pipes = link[2:]
        programs[prog] = pipes
    print programs
    checked = []
    connected = ['0']
    while len(connected) > 0:
        print "Start - checked", checked, "connected ", connected
        checking = connected[0]
        links = programs[connected[0]]
        print links
        for link in links:
            if link not in checked and link not in connected:
                connected.append(link)
        checked.append(connected[0])
        connected.remove(connected[0])
        print "Finished - checked", checked, "connected ", connected
        
    return len(checked)


def solve2(inlist):
    programs = {}
    for link in inlist:
        link = link.replace(",", "")
        link = link.split(" ")
        prog = link[0]
        pipes = link[2:]
        programs[prog] = pipes
    print programs
    groups = 0

    unlinked = range(len(programs))
    print unlinked
    while len(unlinked) > 0:
        checked = []
        connected = programs[(str)(unlinked[0])]
        while len(connected) > 0:
            print "Start - checked", checked, "connected ", connected
            checking = connected[0]
            links = programs[connected[0]]
            print links
            for link in links:
                if link not in checked and link not in connected:
                    connected.append(link)
            checked.append(connected[0])
            connected.remove(connected[0])
            print "Finished - checked", checked, "connected ", connected
        for prog in checked:
            unlinked.remove((int)(prog))
        groups = groups + 1
    return groups


with open('inputs/12in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')

#print test
#print solve1(test)
print solve2(test)

