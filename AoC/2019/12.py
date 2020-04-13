from copy import deepcopy
from math import gcd

testinputs = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

testinputs = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

def a(inputs):
    # Read input
    inputs = inputs.split("\n")
    moon_pos = []
    for moon in inputs:
        coords = moon.split(",")
        x = int(coords[0][3:])
        y = int(coords[1][3:])
        z = int(coords[2][3:-1])
        moon_pos.append([x,y,z])

    moon_velocity = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    
    periods = 1000
    #print(moon_pos, moon_velocity)
    for _ in range(periods):
        # Update Velocities
        for i_moon in range(len(moon_velocity)):
            for j_moon in range(len(moon_pos)):
                if i_moon != j_moon:
                    moon_velocity[i_moon][0] += positive(moon_pos[j_moon][0] - moon_pos[i_moon][0])
                    moon_velocity[i_moon][1] += positive(moon_pos[j_moon][1] - moon_pos[i_moon][1])
                    moon_velocity[i_moon][2] += positive(moon_pos[j_moon][2] - moon_pos[i_moon][2])
        
        # Update Positions
        for moon in range(len(moon_pos)):
            moon_pos[moon][0] += moon_velocity[moon][0]
            moon_pos[moon][1] += moon_velocity[moon][1]
            moon_pos[moon][2] += moon_velocity[moon][2]
        
    # Calculate Energy
    total_energy = 0
    for moon in range(len(moon_pos)):
        pe = abs(moon_pos[moon][0]) + abs(moon_pos[moon][1]) + abs(moon_pos[moon][2])
        ke = abs(moon_velocity[moon][0]) + abs(moon_velocity[moon][1]) + abs(moon_velocity[moon][2])
        #print(moon, ke, pe, ke*pe)
        total_energy += (pe*ke)

    #print(moon_pos, moon_velocity, total_energy)
    return total_energy

def positive(i):
    if i > 0:
        return 1
    if i == 0:
        return 0
    if i < 0:
        return - 1

def b(inputs):
    # Get LCM of each axis' period
    # Read input
    inputs = inputs.split("\n")
    moon_pos = []
    for moon in inputs:
        coords = moon.split(",")
        x = int(coords[0][3:])
        y = int(coords[1][3:])
        z = int(coords[2][3:-1])
        moon_pos.append([x,y,z])
    start_pos = deepcopy(moon_pos)
    moon_velocity = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
    start_velocity = deepcopy(moon_velocity)
    periods = []
    for i in range(3):
        period_count = 1
        #print(moon_pos, moon_velocity)
        found = False
        while not found:
            # Update Velocities
            for i_moon in range(len(moon_velocity)):
                for j_moon in range(len(moon_pos)):
                    if i_moon != j_moon:
                        moon_velocity[i_moon][i] += positive(moon_pos[j_moon][i] - moon_pos[i_moon][i])
            # Update Positions
            for moon in range(len(moon_pos)):
                moon_pos[moon][i] += moon_velocity[moon][i]
            
            
            if moon_velocity == start_velocity and moon_pos == start_pos:
                found = True
            else:
                period_count += 1

        periods.append(period_count)
    lcm = periods[0]
    for i in periods[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


with open('inputs/12in.txt', 'r') as infile:
    inputs = infile.read()


#print(a(testinputs))
#print(a(inputs))

#print(b(testinputs))
print(b(inputs))
