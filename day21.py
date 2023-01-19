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
    (13,0,1),
    (31,0,2),
    (53,0,3),
    (75,0,4),
    (102,0,5)
]

rings = [
    (25,1,0),
    (50,2,0),
    (100,3,0),
    (20,0,1),
    (40,0,2),
    (80,0,3)
]

def read():    
    with open("inputs/day21.txt", mode="+r", encoding="utf-8") as f:
        return tuple(int(c) for c in f.read().strip())

def part1(stdscrn, vis=False):
    playerhp = 8
    boss_stats =  read()
    
def part2(stdscrn, vis=False):
    inpt = read()

if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    part1(stdscr, vis=True)
    #part2(stdscr, vis=True)


"""
Hit Points: 103
Damage: 9
Armor: 2
"""