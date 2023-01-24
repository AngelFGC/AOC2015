from time import sleep
import curses
import itertools
import math
import random
from typing import Dict, List, Set, Tuple, Iterable
from collections import deque
from functools import cache
from copy import deepcopy

def sample() -> List[int]:
    return list(range(1,6)) + list(range(7,12))

def read() -> List[int]:
    with open("inputs/day24.txt", mode="+r", encoding="utf-8") as f:
        return [int(l.strip()) for l in f]

def areWeightsValid(weights:Tuple[int], rem:List[int], cap:int) -> bool:
    if not rem:
        return True
    elif rem[0] > max(cap - w for w in weights if w < cap):
        return False
    else:
        next_gift = rem[-1]
        next_rem = rem[:-1]

        for i in range(1, len(weights)):
            if next_gift <= (cap - weights[i]):
                # put in i
                new_weights = tuple(
                    w + next_gift if j == i else w
                    for j,w in enumerate(weights)
                )
                if areWeightsValid(new_weights, next_rem, cap):
                    return True
        return False

def quantumEntangle(L:Iterable[int]) -> int:
    x = 1
    for y in L:
        x *= y
    return x

def solve(presents:List[int], compartments:int):
    cap = sum(presents) // compartments
    fscandidates = []
    i = 1

    while not fscandidates:
        i += 1
        fscandidates = [
            combo for combo in itertools.combinations(presents, i)
            if sum(combo) == cap
        ]

    fscandidates.sort(key=quantumEntangle)
    
    for frontSeat in fscandidates:
        new_weights = (sum(frontSeat),) + tuple([0] * (compartments-1))
        remainingpresents = list(set(presents).difference(frontSeat))
        remainingpresents.sort(reverse=True)
        weightsValid =  areWeightsValid(
            new_weights, remainingpresents, cap
        )
        if weightsValid:
            return quantumEntangle(frontSeat)
    return -1

def part1(stdscrn, vis=False):
    #presents = sample()
    presents = read()
    print(solve(presents, 3))
    
def part2(stdscrn, vis=False):
    #presents = sample()
    presents = read()
    print(solve(presents, 4))

if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    part1(stdscr, vis=True)
    part2(stdscr, vis=True)
