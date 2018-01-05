sample1 ='''Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.'''


def parseinput(inlist):
    startstate = inlist.split('\n')[0][-2]
    steps = inlist.split('\n')[1]
    steps = (int)(steps.split(' ')[-2])
    #print startstate, steps
    statelist = inlist.split('In state ')[1:]
    states = []
    for state in statelist:
        statedict = {}
        statedict['name'] = state[0]
        zerowrite = state.split('\n')[2][-2]
        zerolr = (state.split('\n')[3]).split(' ')[-1][:-1]
        zeronext = state.split('\n')[4][:-2]
        statedict['zero'] = {'write':zerowrite,'dir':zerolr, 'next':zeronext} 
        statedict['one'] = {}
        states.append(statedict)
    print states
    return states

def solve1(inlist):
    parseinput(inlist)
    return 

def solve2(inlist):
    return

with open('20in.txt', 'r') as infile:
    test = infile.read()

test = sample1

print test
print solve1(test)
#print solve2(test)

