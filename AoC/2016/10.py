sample1='''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''

class Bot:
    botid = None
    lower = None
    higher = None
    held = []
    def __init__(self, botid, lower=lower, higher=higher, held=held):
        self.botid = botid
        self.lower = lower
        self.higher = higher
        self.held = held
    def __repr__(self):
        result = "<Bot- id: %s, lower: %s, higher: %s, held %s>"%(self.botid, self.lower, self.higher, self.held)
        return result

def readinput(intext):
    bots = []
    for thisline in intext:
        line = thisline.split()
        if line[0] == 'value':
            added = False
            for bot in bots:
                if bot.botid == line[-1]:
                    #print line, "match" , bot.botid, line[-1], line[1]
                    bot.held.append((int)(line[1]))
                    added = True
            if not added:
                #print line, "creating" , line[-1], line[1]
                newbot = Bot(line[-1],held=[(int)(line[1])])
                bots.insert(0, newbot)
        else:
            added = False
            for bot in bots:
                if bot.botid == line[1]:
                    bot.lower = (line[5],line[6])
                    bot.higher = (line[-2],line[-1])
                    added = True
            if not added:
                newbot = Bot(line[1],held=[],lower=(line[5],line[6]),higher=(line[-2],line[-1]))
                bots.insert(0, newbot)
    return bots

def solve1(intext):
    bots = readinput(intext)
    output = {}
    solution = ""
    unsolved = True
    #print bots
    while unsolved:
        moving = False
        for bot in bots:
            #print bot.held
            if len(bot.held) == 2:
                print bots
                moving = True
                if bot.held == [17,61] or bot.held == [61,17]:
                    unsolved = False
                    solution = bot.botid
                #print bot, bot.higher
                if bot.higher[0] == "bot":
                    added = False
                    for newhigh in bots:
                        if newhigh.botid == bot.higher[1]:
                            newhigh.held.append(max(bot.held))
                            added = True
                    if not added:
                         newbot = Bot(bot.higher[0],held=[max(bot.held)])
                         bots.insert(0, newbot)
                else:
                    print "bot", bot.botid, "outputting", max(bot.held)
                
                if bot.lower[0] == "bot":
                    added = False
                    for newlow in bots:
                        if newlow.botid == bot.lower[1]:
                            newlow.held.append(min(bot.held))
                            added = True
                    if not added:
                         newbot = Bot(bot.lower[0],held=[min(bot.held)])
                         bots.insert(0, newbot)
                else:
                    print "bot", bot.botid, "outputting", min(bot.held)
                bot.held = []
        if moving == False:
            unsolved = False
            print "Stalled"
            print bots
    return solution

def solve2(intext):
    bots = readinput(intext)
    outputs = []
    #print bots
    moving = True
    while moving:
        moving = False
        for bot in bots:
            #print bot.held
            if len(bot.held) == 2:
                #print bots
                moving = True
                #print bot, bot.higher
                if bot.higher[0] == "bot":
                    added = False
                    for newhigh in bots:
                        if newhigh.botid == bot.higher[1]:
                            newhigh.held.append(max(bot.held))
                            added = True
                    if not added:
                         newbot = Bot(bot.higher[0],held=[max(bot.held)])
                         bots.insert(0, newbot)
                else:
                    #print "bot", bot.botid, "outputting", max(bot.held), "to output", bot.higher[1]
                    if (int)(bot.higher[1]) < 3:
                        outputs.append(max(bot.held))
                    
                if bot.lower[0] == "bot":
                    added = False
                    for newlow in bots:
                        if newlow.botid == bot.lower[1]:
                            newlow.held.append(min(bot.held))
                            added = True
                    if not added:
                         newbot = Bot(bot.lower[0],held=[min(bot.held)])
                         bots.insert(0, newbot)
                else:
                    #print "bot", bot.botid, "outputting", min(bot.held), "to output", bot.lower[1]
                    if (int)(bot.lower[1]) < 3:
                        outputs.append(min(bot.held))
                bot.held = []

    total = 1
    print outputs
    for output in outputs:
        total = total * output
    return total


with open('inputs/10in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
tests = tests.split('\n')
#print tests

#print solve1(tests)
print solve2(tests)
