import re

sample1 ='''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''

def dictize(inlist):
    dictlist = []
    for i in inlist:
        name = i.split(' ')[0]
        weight = re.search('(?<=\().+?(?=\))',i).group(0)
        links = []
        if '->'in i:
            #print ''.join(i.split())
            links = ''.join(i.split()).strip(' ').split('->')[1].split(',')
        dictlist.append({'weight': weight, 'links': links, 'name': name})
        #print name, weight, links
    return dictlist

def solve1(inlist):
    tower = dictize(inlist)
    base = list(tower)
    #print "tower", len(tower), tower
    for program in tower:
        #print "testing", program['name']
        if len(program['links']) == 0:
            for i in base:
                #print program['name']
                if i['name'] == program['name']:
                    base.remove(i)
                    #print "removing", i
            
        else:
            for link in program['links']:
                for i in base:
                    if i['name'] == link:
                        base.remove(i)
                        #print "removing", i
                    
    #print base
    return base[0]['name']

def solve2(inlist):
    base = solve1(inlist)
    tower = dictize(inlist)
    #fill out towerweights
    towerweight(tower, base)
    print tower
    findimbalance(tower, base)
    return 

def findimbalance(tower, base):
    searching = True
    current = base
    while searching:     
        for i in tower:
            if i['name'] == current:
                print "diff" , i['diff']
                found = True
                for link in i['links']:
                    for j in tower:
                        if j['name'] == link:
                            print j['name'], j['balanced'], j['treeweight'], j['weight']
                            if j['balanced'] == False:
                                found = False
                                current = link
        if found:
            searching = False


                #if not link['balanced']:
                    #findimbalance(tower, link['name'])

def towerweight(tower, name):
    weight = 0
    for i in tower:
        if i['name'] == name:
            weight = i['weight']
            i['balanced'] = True
            if len(i['links']) != 0:
                linkweights = []
                for link in i['links']:
                    linkweight = (int)(towerweight(tower, link))
                    linkweights.append(linkweight) 
                    weight = (int)(weight) + linkweight

                matcher = linkweights[0]
                for match in linkweights:
                    if match != matcher:
                        i['balanced'] = False
                        i['diff'] = abs(match - matcher)
            i['treeweight'] = weight
    return weight


with open('inputs/7in.txt', 'r') as infile:
    test = infile.read()

#test = sample1
test = test.split('\n')

print test
print solve1(test)
print solve2(test)

