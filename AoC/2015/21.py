from itertools import combinations, permutations

sample1=''''''

weapons = {
"Dagger"    :(8,4,0),
"Shortsword":(10,5,0),
"Warhammer" :(25,6,0),
"Longsword" :(40,7,0),
"Greataxe"  :(74,8,0),
}
armors = {
"None"        :(0,0,0),
"Leather"     :(13,0,1),
"Chainmail"   :(31,0,2),
"Splintmail"  :(53,0,3),
"Bandedmail"  :(75,0,4),
"Platemail"   :(102,0,5),
}
rings = {
"Damage +1" :(25,1,0),
"Damage +2" :(50,2,0),
"Damage +3" :(100,3,0),
"Defense +1":(20,0,1),
"Defense +2":(40,0,2),
"Defense +3":(80,0,3),
}
#(76, 6, 3) Warhammer Chainmail ['Defense +1']

def battle(player, boss):
    playerhp = player[0]
    bosshp = boss[0]
    playerdpt = player[1] - boss[2]
    bossdpt = boss[1] - player[2]
    if playerdpt < 1:
        playerdpt = 1
    if bossdpt < 1:
        bossdpt = 1
    while True:
        bosshp -= playerdpt
        if bosshp < 1 :
            #print player, boss, playerdpt, bossdpt
            return True
        else:
            playerhp -= bossdpt
            if playerhp < 1:
                return False

def equip(weapon, armor, ring):
    cost = weapons[weapon][0] + armors[armor][0]
    damage = weapons[weapon][1] + armors[armor][1]
    defence = weapons[weapon][2] + armors[armor][2]
    for i in ring:
        #print rings[ring]
        cost += rings[i][0]
        damage += rings[i][1]
        defence += rings[i][2]
    return (cost,damage,defence)

def solve1(weapons, armors, rings, intext):
    #print weapons, rings, armor
    split = intext.split('\n')
    bosshp = (int)(split[0].split()[-1])
    bossdmg =  (int)(split[1].split()[-1])
    bossarmor =  (int)(split[2].split()[-1])
    bossstats = (bosshp,bossdmg,bossarmor)
    mincost = 0
    ringcombos = [[]]
    ringcombos.extend(permutations(rings,1))
    ringcombos.extend(permutations(rings,2))
    ringcombos = [list(i) for i in ringcombos]
    mincost = 1000
    for weapon in weapons:
        for armor in armors:
            for ring in ringcombos:
                player = equip(weapon, armor, ring)
                cost = player[0]
                if cost < mincost:
                    playerstats = (100,player[1],player[2])
                    if battle(playerstats, bossstats):
                        mincost = cost
                        #print player, weapon, armor, ring
    return mincost

def solve2(weapons,armors,rings, intext):
    #print weapons, rings, armor
    split = intext.split('\n')
    bosshp = (int)(split[0].split()[-1])
    bossdmg =  (int)(split[1].split()[-1])
    bossarmor =  (int)(split[2].split()[-1])
    bossstats = (bosshp,bossdmg,bossarmor)
    mincost = 0
    ringcombos = [[]]
    ringcombos.extend(permutations(rings,1))
    ringcombos.extend(permutations(rings,2))
    ringcombos = [list(i) for i in ringcombos]
    maxcost = 0
    for weapon in weapons:
        for armor in armors:
            for ring in ringcombos:
                player = equip(weapon, armor, ring)
                cost = player[0]
                if cost > maxcost:
                    playerstats = (100,player[1],player[2])
                    if not battle(playerstats, bossstats):
                        maxcost = cost
                        #print player, weapon, armor, ring
    return maxcost


with open('inputs/21in.txt', 'r') as infile:
    tests = infile.read()

print tests

print solve1(weapons,armors,rings,tests)
print solve2(weapons,armors,rings,tests)
