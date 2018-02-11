sample1='''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''

def distance(reindeer, time):
    speed = reindeer[0]
    uptime = reindeer[1]
    downtime = reindeer[2]
    distance = speed*uptime*(time / (uptime + downtime))
    remainingtime = time % (uptime + downtime)
    if remainingtime > uptime:
        distance += uptime*speed
    else:
        distance += remainingtime*speed
    return distance


def solve1(intext):
    time = 2503
    furthest = 0
    for line in intext:
        split = line.split()
        speed = (int)(split[3])
        uptime = (int)(split[6])
        downtime = (int)(split[-2])
        distance = speed*uptime*(time / (uptime + downtime))
        remainingtime = time % (uptime + downtime)
        if remainingtime > uptime:
            distance += uptime*speed
        else:
            distance += remainingtime*speed

        #print speed, uptime, downtime, distance
        if distance > furthest:
            furthest = distance
    return furthest

def solve2(intext):
    time = 2503
    furthest = 0
    reindeers = []
    for line in intext:
        split = line.split()
        speed = (int)(split[3])
        uptime = (int)(split[6])
        downtime = (int)(split[-2])
        reindeers.append((speed,uptime,downtime))
    #print reindeers
    scores = [0 for i in range(len(reindeers))]
    for i in range(1,time):
        furthest = 0
        winning = 0
        for reindeer in range(len(reindeers)):
            sofar = distance(reindeers[reindeer], i)
            if sofar > furthest:
                furthest = sofar
                winning = reindeer
        scores[winning]+= 1
    #print scores
    return max(scores)


with open('inputs/14in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests
tests = tests.split('\n')

print solve1(tests)
print solve2(tests)
