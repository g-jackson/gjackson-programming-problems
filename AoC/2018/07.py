testinputs = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

def a(inputs):
    dependancies = {}
    for input in inputs:
        before = input.split()[1]
        after = input.split()[7]
        if before not in dependancies:
            dependancies[before] = []
        if after not in dependancies:
            dependancies[after] = [before]
        else:
            dependancies[after].append(before)

    result = ""
    # Remove nodes until none remain
    for _ in range(len(dependancies)):
        remove_letter = "Z"
        # Find next node to remove
        for node in dependancies:
            if dependancies[node] == [] and node < remove_letter:
                remove_letter = node

        result += remove_letter

        # Remove node and remove from all dependancies
        del dependancies[remove_letter]
        for node in dependancies:
            if remove_letter in dependancies[node]:
                dependancies[node].remove(remove_letter)

    return result

def b(inputs):
    dependancies = {}
    for input in inputs:
        before = input.split()[1]
        after = input.split()[7]
        if before not in dependancies:
            dependancies[before] = []
        if after not in dependancies:
            dependancies[after] = [before]
        else:
            dependancies[after].append(before)

    second = 0
    workers = 5
    time_remaining = {}
    while (dependancies != {}) or (time_remaining != {}):
        # Start tasks
        task_ready = True
        while workers != 0 and task_ready:
            remove_letter = chr(91)
            for node in dependancies:
                if dependancies[node] == [] and node < remove_letter:
                    remove_letter = node
            if remove_letter == chr(91):
                task_ready = False
            else:
                workers -= 1
                del dependancies[remove_letter]
                time_remaining[remove_letter] = ord(remove_letter) - 64 + 60
        
        # print(second, time_remaining, dependancies)
        # Count down any tasks in progress
        del_nodes = []
        for node in time_remaining:
            time_remaining[node] -= 1
            # Remove from all dependancies if task done
            if time_remaining[node] == 0:
                for dependancy in dependancies:
                    if node in dependancies[dependancy]:
                        dependancies[dependancy].remove(node)
                del_nodes = node
                workers += 1
        for node in del_nodes:
            del time_remaining[node]
        second += 1
    return second


with open('inputs/07in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split("\n")


#print(a(inputs))
#print(b(testinputs.split("\n")))
print(b(inputs))
