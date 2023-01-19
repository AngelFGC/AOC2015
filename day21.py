from time import sleep
import curses
import itertools
import math
import random
from typing import Dict, List, Set, Tuple, Iterable
from collections import deque
from functools import cache

"""
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""

weapons = [
    (8,4,0),
    (10,5,0),
    (25,6,0),
    (40,7,0),
    (74,8,0)
]

armors = [
    (0,0,0),
    (13,0,1),
    (31,0,2),
    (53,0,3),
    (75,0,4),
    (102,0,5)
]

rings = [
    (0,0,0),
    (0,0,0),
    (25,1,0),
    (50,2,0),
    (100,3,0),
    (20,0,1),
    (40,0,2),
    (80,0,3)
]

def read():    
    with open("inputs/day21.txt", mode="+r", encoding="utf-8") as f:
        return tuple(int(c) for c in f.read().strip().split(","))

def getTurnsToWin(pHP, pAtk, pDef, boss):
    bHP, bAtk, bDef = boss
    return (
        math.ceil(bHP/max(1, pAtk - bDef)),
        math.ceil(pHP/max(1, bAtk - pDef))
    )

def part1(stdscrn, vis=False):
    playerhp = 100
    boss_stats =  read()

    mincost = float("+inf")
    mingear = None

    for (i, wpn), (j, arm), ((k1, hand1), (k2, hand2)) in itertools.product(
        enumerate(weapons), enumerate(armors), 
        itertools.combinations(enumerate(rings), 2)
    ):
        cost = wpn[0] + arm[0] + hand1[0] + hand2[0]
        t2Win, t2Lose = getTurnsToWin(
            playerhp, wpn[1] + arm[1] + hand1[1] + hand2[1],
            wpn[2] + arm[2] + hand1[2] + hand2[2], boss_stats
        )

        if t2Win <= t2Lose:
            if cost < mincost:
                mincost = cost
                mingear = (i,j-1, k1-2, k2-2)

    print(mincost)
    print(mingear)
    
def part2(stdscrn, vis=False):
    playerhp = 100
    boss_stats =  read()

    maxcost = float("-inf")
    maxgear = None

    for (i, wpn), (j, arm), ((k1, hand1), (k2, hand2)) in itertools.product(
        enumerate(weapons), enumerate(armors), 
        itertools.combinations(enumerate(rings), 2)
    ):
        cost = wpn[0] + arm[0] + hand1[0] + hand2[0]
        t2Win, t2Lose = getTurnsToWin(
            playerhp, wpn[1] + arm[1] + hand1[1] + hand2[1],
            wpn[2] + arm[2] + hand1[2] + hand2[2], boss_stats
        )

        if t2Win > t2Lose:
            if cost > maxcost:
                maxcost = cost
                maxgear = (i,j-1, k1-2, k2-2)

    print(maxcost)
    print(maxgear)

if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    part1(stdscr, vis=True)
    part2(stdscr, vis=True)
