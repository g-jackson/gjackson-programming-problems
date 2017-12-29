sample1 ='''p=<3,0,0>, v=<2,0,0>, a=<-1,0,0>
p=<4,0,0>, v=<0,0,0>, a=<-2,0,0>'''


# Pretty hacky, assumes the closest point resolves quickly
def solve1(inlist):
    minimum = 1000000000
    ticks = 2000
    counter = 0
    minpoint = 0
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
        for i in range(ticks):
            newdistance = abs(p[0]+ (v[0] + ticks*a[0])) + abs(p[1]+ (v[1] + ticks*a[1])) + abs(p[2]+ (v[2] + ticks*a[2]))
            
        print newdistance
        if newdistance < minimum:
            minimum = newdistance
            minpoint = counter
        counter = counter + 1
    return minpoint

def solve2(inlist):
    minimum = 1000000000
    ticks = 2000
    counter = 0
    minpoint = 0
    particles = []
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
        particles.append([p,v,a])    
    print particles

    for tick in range(ticks):
        tickpoints = []
        for particle in particles:
            tickpoints[] = 
    return



with open('20in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')

#print test
#print solve1(test)
print solve2(test)

