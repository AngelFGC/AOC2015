from time import sleep
import curses
import itertools
import math
import random
from typing import Dict, List, Set, Tuple, Iterable
from collections import deque
from functools import cache
from copy import deepcopy

"""
Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
"""

spells = [
    {"name":"Magic Missile", "cost":53, "type":"instant", "result":{"damage":4}},
    {"name":"Drain", "cost":73, "type":"instant", "result":{"damage":2, "heal":2}},
    {"name":"Shield", "cost":113, "type":"effect", "result":{"armor":7, "duration":6}},
    {"name":"Poison", "cost":173, "type":"effect", "result":{"damage":3, "duration":6}},
    {"name":"Recharge", "cost":229, "type":"effect", "result":{"mana":101, "duration":5}},
]

def read():    
    with open("inputs/day22.txt", mode="+r", encoding="utf-8") as f:
        return tuple(int(c) for c in f.read().strip().split(","))

def runTurnPart1(player:List, boss:List, currFX:Dict, spellid:int):
    pHP, pMana = player[0], player[1]
    bHP, bDMG = boss[0], boss[1]
    pArmor = 0
    # Player Turn
    # Apply Effects
    # if currFX["armor"] > 0:
    #     pArmor = spells[2]["result"]["armor"]
    if currFX["damage"] > 0:
        bHP -= spells[3]["result"]["damage"]
    if currFX["mana"] > 0:
        pMana += spells[4]["result"]["mana"]
    for effect in currFX:
        if currFX[effect] > 0:
            currFX[effect] -= 1
    # Cast Spell
    spl = spells[spellid]
    if spl["type"] == "instant":
        bHP -= spl["result"]["damage"]
        if "heal" in spl["result"]:
            pHP += spl["result"]["heal"]
    else:
        eff = spl["result"]
        tpe = set(eff.keys())
        tpe.remove("duration")
        tpe = tpe.pop()

        if currFX[tpe] != 0:
            return None
        else:
            currFX[tpe] = spl["result"]["duration"]

    pMana -= spl["cost"]

    if bHP > 0:
        # Boss TUrn
       # Apply Player Effects
        if currFX["armor"] > 0:
            pArmor = spells[2]["result"]["armor"]
        if currFX["damage"] > 0:
            bHP -= spells[3]["result"]["damage"]
        if currFX["mana"] > 0:
            pMana += spells[4]["result"]["mana"]
        for effect in currFX:
            if currFX[effect] > 0:
                currFX[effect] -= 1

        # Damage
        if bHP > 0:
            pHP -= max(1, (bDMG - pArmor))
    
    player[:] = (pHP, pMana)
    boss[:] = (bHP, bDMG)
    return spl["cost"]


def runTurnPart2(player:List, boss:List, currFX:Dict, spellid:int):
    player[0] -= 1
    if player[0] == 0:
        return spells[spellid]["cost"]
    else:
        return runTurnPart1(player, boss, currFX, spellid)

def part1(stdscrn, vis=False):
    boss =  read()
    player = (50,500)

    q = deque()
    pInit = list(player)
    bInit = list(boss)
    effInit = {
        "damage": 0,
        "armor": 0,
        "mana": 0
    }
    q.append((pInit, bInit, effInit, 0, []))

    min_cost = float("+inf")
    spell_act = []

    while q:
        pStats, bStats, currEff, pathCost, spellOrdr = q.pop()
        for i in range(len(spells)):
            pNext = deepcopy(pStats)
            bNext = deepcopy(bStats)
            effNext = deepcopy(currEff)
            splOrdrNext = deepcopy(spellOrdr) + [i]
            if pNext[1] >= spells[i]["cost"]:
                cstNext = runTurnPart1(pNext, bNext, effNext, i)
                if cstNext is None:
                    continue
                cstNext += pathCost
                if cstNext >= min_cost:
                    continue
                if pNext[0] <= 0:
                    continue
                if bNext[0] <= 0:
                    if cstNext < min_cost:
                        min_cost = cstNext
                        spell_act = splOrdrNext
                        continue
                q.append((pNext, bNext, effNext, cstNext, splOrdrNext))
    print(min_cost)
    print(spell_act)

    
def part2(stdscrn, vis=False):
    boss =  read()
    player = (50,500)

    q = deque()
    pInit = list(player)
    bInit = list(boss)
    effInit = {
        "damage": 0,
        "armor": 0,
        "mana": 0
    }
    q.append((pInit, bInit, effInit, 0, []))

    min_cost = float("+inf")
    spell_act = []

    while q:
        pStats, bStats, currEff, pathCost, spellOrdr = q.pop()
        for i in range(len(spells)):
            pNext = deepcopy(pStats)
            bNext = deepcopy(bStats)
            effNext = deepcopy(currEff)
            splOrdrNext = deepcopy(spellOrdr) + [i]
            if pNext[1] >= spells[i]["cost"]:
                cstNext = runTurnPart2(pNext, bNext, effNext, i)
                if cstNext is None:
                    continue
                cstNext += pathCost
                if cstNext >= min_cost:
                    continue
                if pNext[0] <= 0:
                    continue
                if bNext[0] <= 0:
                    if cstNext < min_cost:
                        min_cost = cstNext
                        spell_act = splOrdrNext
                        continue
                q.append((pNext, bNext, effNext, cstNext, splOrdrNext))
    print(min_cost)
    print(spell_act)

if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    part1(stdscr, vis=True)
    part2(stdscr, vis=True)
