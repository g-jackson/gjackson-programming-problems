import collections
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
        zerowrite = (int)(state.split('\n')[2][-2])
        zerolr = (state.split('\n')[3]).split(' ')[-1][:-1]
        zeronext = state.split('\n')[4][-2]
        onewrite =  (int)(state.split('\n')[6][-2])
        onelr = (state.split('\n')[7]).split(' ')[-1][:-1]
        onenext = state.split('\n')[8][-2]
        statedict['zero'] = {'write':zerowrite,'dir':zerolr, 'next':zeronext} 
        statedict['one'] = {'write':onewrite,'dir':onelr, 'next':onenext}
        states.append(statedict)
    return startstate, steps, states

def runstep(strip, startstate, states, startpos):
    for state in states:
        if state['name'] == startstate:
            # read strip
            if strip[startpos] == 0:
                instructions = state['zero']
            else:
                instructions = state['one']
            #print instructions
            # write strip
            strip[startpos] = instructions['write']
            # update state
            newstate = instructions['next']
            # move strip
            if instructions['dir'] == 'left':
                if startpos != 0:
                    startpos = startpos - 1
                else:
                    strip.appendleft(0)
            else:
                startpos = startpos + 1
                if startpos == len(strip):
                    strip.append(0)

    startstate = newstate
    return startpos, startstate

def solve1(inlist):
    startstate, steps, states = parseinput(inlist)
    startpos = 0
    strip = collections.deque()
    strip.append(0)
    print states
    for i in range(steps):
        startpos, startstate = runstep(strip, startstate, states, startpos)
        #print startstate, startpos, strip

    return strip.count(1)

def solve2(inlist):
    return

with open('25in.txt', 'r') as infile:
    test = infile.read()

#test = sample1

print test
print solve1(test)
#print solve2(test)

