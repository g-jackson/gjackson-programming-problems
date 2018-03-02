sample1=''''''

def bossturn(s):
    # Apply poison
    if s["poison"]:
        s["bosshp"] -= 3
    
    # Apply recharge
    if s["recharge"]:
        s["mana"] += 101
    
    # Turn counters
    s["poison"] = max(0, s["poison"]-1)
    s["shield"] = max(0, s["shield"]-1)
    s["recharge"] = max(0, s["recharge"]-1)

    if s["shield"]:
        s["hp"] -= max(1,s["bossdmg"]-7)
    else:
        s["hp"] -= s["bossdmg"]
    return s

def solve1(intext):
    playerhp = 50
    playermana = 500
    bosshp = intext.split('\n')[0]
    bosshp = (int)(bosshp.split()[-1])
    bossdmg = intext.split('\n')[1]
    bossdmg = (int)(bossdmg.split()[-1])
    print bosshp, bossdmg
    sample = False
    if sample:
        playerhp = 10
        playermana = 250
        bosshp = 14#13
        bossdmg = 8
    state = {"hp":playerhp, "mana": playermana, "bosshp": bosshp, "bossdmg": bossdmg, "manaspent":0, "poison":0, "shield":0, "recharge":0, "cast": ""}
    bfs = [state]
    print bfs
    minmana = 10000000
    winningcombo = ""
    while len(bfs) != 0:
        s = bfs.pop(0)

        #print len(bfs)
        # End Conditions
        if s["manaspent"] > minmana:
            continue
        if s["bosshp"] < 1:
            print "boss killed"
            minmana = s["manaspent"]
            winningcombo = s["cast"]
            continue
        if s["hp"] < 1:
            "player killed"
            continue
        #print s
        
        # Apply poison
        if s["poison"]:
            s["bosshp"] -= 3
        
        # Apply recharge
        if s["recharge"]:
            s["mana"] += 101
        
        # Turn counters
        s["poison"] = max(0, s["poison"]-1)
        s["shield"] = max(0, s["shield"]-1)
        s["recharge"] = max(0, s["recharge"]-1)

        # Magic Missile
        if s["mana"] >= 53:
            news = s.copy()
            news["cast"] += "MM "
            news["mana"] -= 53
            news["manaspent"] += 53
            news["bosshp"] -= 4
            bfs.append(bossturn(news))
        # Drain
        if s["mana"] >= 73:
            news = s.copy()
            news["cast"] += "Drain "
            news["mana"] -= 73
            news["manaspent"] += 73
            news["bosshp"] -= 2
            news["hp"] += 2
            bfs.append(bossturn(news))
        # Shield
        if s["mana"] >= 113 and s["shield"] == 0:
            news = s.copy()
            news["cast"] += "Shield "
            news["mana"] -= 113
            news["manaspent"] += 113
            news["shield"] = 6
            bfs.append(bossturn(news))
        # Poison
        if s["mana"] >= 173 and s["poison"] == 0:
            news = s.copy()
            news["cast"] += "Poison "
            news["mana"] -= 173
            news["manaspent"] += 173
            news["poison"] = 6
            bfs.append(bossturn(news))
        # Recharge
        if s["mana"] >= 229 and s["recharge"] == 0:
            news = s.copy()
            news["cast"] += "Recharge "
            news["mana"] -= 229
            news["manaspent"] += 229
            news["recharge"] = 5
            bfs.append(bossturn(news))

    print winningcombo
    return minmana

def solve2(intext):
    playerhp = 50
    playermana = 500
    bosshp = intext.split('\n')[0]
    bosshp = (int)(bosshp.split()[-1])
    bossdmg = intext.split('\n')[1]
    bossdmg = (int)(bossdmg.split()[-1])
    print bosshp, bossdmg
    sample = False
    if sample:
        playerhp = 10
        playermana = 250
        bosshp = 14#13
        bossdmg = 8
    state = {"hp":playerhp, "mana": playermana, "bosshp": bosshp, "bossdmg": bossdmg, "manaspent":0, "poison":0, "shield":0, "recharge":0, "cast": ""}
    bfs = [state]
    print bfs
    minmana = 10000000
    winningcombo = ""
    while len(bfs) != 0:
        s = bfs.pop(0)
        # End Conditions
        if s["manaspent"] > minmana:
            continue
        # Check boss death first, we can then ignore if the boss last attack kills us if boss died first
        if s["bosshp"] < 1:
            print "boss killed"
            minmana = s["manaspent"]
            winningcombo = s["cast"]
            continue
        # Check if boss killed player
        if s["hp"] < 1:
            continue
        # Check if HM tick killed
        s["hp"] -= 1
        if s["hp"] < 1:
            #print "player killed by tick"
            continue
        #print s
        
        # Apply poison
        if s["poison"]:
            s["bosshp"] -= 3
        
        # Apply recharge
        if s["recharge"]:
            s["mana"] += 101
        
        # Turn counters
        s["poison"] = max(0, s["poison"]-1)
        s["shield"] = max(0, s["shield"]-1)
        s["recharge"] = max(0, s["recharge"]-1)

        # Magic Missile
        if s["mana"] >= 53:
            news = s.copy()
            news["cast"] += "MM "
            news["mana"] -= 53
            news["manaspent"] += 53
            news["bosshp"] -= 4
            bfs.append(bossturn(news))
            #endstate = bossturn(hp, mana, bosshp, bossdmg, manaspent, poison, shield, recharge)
        # Drain
        if s["mana"] >= 73:
            news = s.copy()
            news["cast"] += "Drain "
            news["mana"] -= 73
            news["manaspent"] += 73
            news["bosshp"] -= 2
            news["hp"] += 2
            bfs.append(bossturn(news))
        # Shield
        if s["mana"] >= 113 and s["shield"] == 0:
            news = s.copy()
            news["cast"] += "Shield "
            news["mana"] -= 113
            news["manaspent"] += 113
            news["shield"] = 6
            bfs.append(bossturn(news))
        # Poison
        if s["mana"] >= 173 and s["poison"] == 0:
            news = s.copy()
            news["cast"] += "Poison "
            news["mana"] -= 173
            news["manaspent"] += 173
            news["poison"] = 6
            bfs.append(bossturn(news))
        # Recharge
        if s["mana"] >= 229 and s["recharge"] == 0:
            news = s.copy()
            news["cast"] += "Recharge "
            news["mana"] -= 229
            news["manaspent"] += 229
            news["recharge"] = 5
            bfs.append(bossturn(news))

    print winningcombo
    return minmana


with open('inputs/22in.txt', 'r') as infile:
    tests = infile.read()

#tests = sample1
#print tests

#print solve1(tests)
print solve2(tests)