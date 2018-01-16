import numpy as np
sample1 ='''p=<-6,0,0>, v=<3,0,0>, a=<0,0,0>
p=<-4,0,0>, v=<2,0,0>, a=<0,0,0>
p=<-2,0,0>, v=<1,0,0>, a=<0,0,0>
p=<3,2,0>, v=<-1,0,0>, a=<0,0,0>
p=<4,2,0>, v=<-1,0,0>, a=<-1,0,0>'''

def readinput(inlist):
    points = []
    for particle in inlist:
        p = particle.split(' ')[0]
        p = p[p.find('<')+1:p.find('>')].split(',')
        p = map(int, p)
        v = particle.split(' ')[1]
        v = v[v.find('<')+1:v.find('>')].split(',')
        v = map(int, v)
        a = particle.split(' ')[2]
        a = a[a.find('<')+1:a.find('>')].split(',')
        a = map(int, a)
        points.append((p,v,a))
    return points

# Pretty hacky, assumes the closest point resolves quickly
def solve1(inlist):
    minimum = 1000000000
    ticks = 4000
    counter = 0
    minpoint = 0
    points = readinput(inlist)
    for point in points:
        p,v,a = point
        newdistance = abs(p[0]+ (v[0] + ticks*a[0])) + abs(p[1]+ (v[1] + ticks*a[1])) + abs(p[2]+ (v[2] + ticks*a[2]))
    
        #print newdistance
        if newdistance < minimum:
            minimum = newdistance
            minpoint = counter
        counter = counter + 1
    return minpoint

def solve2(inlist):
    minimum = 1000000000
    ticks = 100
    counter = 0
    minpoint = 0
    particles = readinput(inlist)
    for tick in range(ticks):
        print tick
        # Update
        for particle in particles:
            #print "before", particle
            particle[1][0] = particle[1][0] + particle[2][0]
            particle[1][1] = particle[1][1] + particle[2][1]
            particle[1][2] = particle[1][2] + particle[2][2]
            particle[0][0] = particle[0][0] + particle[1][0]
            particle[0][1] = particle[0][1] + particle[1][1]
            particle[0][2] = particle[0][2] + particle[1][2]
            #print "after", particle
        
        # Check for particles at same pos now
        for particle in particles:
            matches = [i for i, x in enumerate(particles) if x[0] == particle[0]]
            #print matches
            if len(matches) > 1:
                # Remove in reverse order so indexes stay correct
                matches = matches[::-1]
                print matches
                for match in matches:
                    print "Removing", particles[match]
                    #print "Removing", particles[match]
                    particles.remove(particles[match])
                #particles.remove(particle)
                
    return len(particles)



with open('inputs/20in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')

#print test
#print solve1(test)
print solve2(test)
