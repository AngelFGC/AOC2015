from time import sleep
import curses
import itertools
import math
import random
from typing import Dict, List, Set, Tuple, Iterable
from collections import deque
from functools import cache

@cache
def generateDivisors(x:int):
    divisors = []
    for i in range(1, int(math.sqrt(x) + 1)):
        if x % i == 0:
            yield i
            
            if x != i*i:
                divisors.append(x // i)
    for i in divisors[::-1]:
        yield i

@cache
def generateDivBwd(x:int):
    for i in generateDivisors(x):
        yield x // i

def read():    
    with open("inputs/day20.txt", mode="+r", encoding="utf-8") as f:
        return f.read().strip()

def presentCount(house:int) -> int:
    return sum(x for x in generateDivBwd(house)) * 10

def presentCount2(house:int) -> int:
    def gen(house:int):
        for x in generateDivBwd(house):
            if x*50 < house:
                break
            yield x
            
    return sum(x for x in gen(house)) * 11

def part1(stdscrn, vis=False):
    inpt = int(read())
    
    n = inpt

    if vis:
        stdscr.addstr(0, 0, f"** PART 1  -- TARGET: {n} **\n")
        stdscr.refresh()

    ctr = itertools.count(1)
    pres = 0
    while pres < n:
        i = next(ctr)
        pres = presentCount(i)
        if vis:
            maxy, _ = stdscr.getmaxyx()
            stdscr.addstr(1 + ((i-1) % (maxy-2)), 0, f"House {i:5d}: {pres:9d}\n")
            stdscr.refresh()
    
    stdscr.clear()
    stdscr.addstr(0, 0, f"** PART 1 RESULTS **\n")
    stdscr.addstr(1, 0, f"House {i}, {pres} presents (Bound: {n})\n")
    stdscr.addstr(2, 0, f"Press any key to continue...\n")
    stdscr.getch()
    
def part2(stdscrn, vis=False):
    inpt = int(read())
    
    n = inpt

    if vis:
        stdscr.addstr(0, 0, f"** PART 2  -- TARGET: {n} **\n")
        stdscr.refresh()

    ctr = itertools.count(1)
    pres = 0
    while pres < n:
        i = next(ctr)
        pres = presentCount2(i)
        if vis:
            maxy, _ = stdscr.getmaxyx()
            stdscr.addstr(1 + ((i-1) % (maxy-2)), 0, f"House {i:5d}: {pres:9d}\n")
            stdscr.refresh()
    
    stdscr.clear()
    stdscr.addstr(0, 0, f"** PART 2 RESULTS **\n")
    stdscr.addstr(1, 0, f"House {i}, {pres} presents (Bound: {n})\n")
    stdscr.addstr(2, 0, f"Press any key to continue...\n")
    stdscr.getch()

if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    part1(stdscr, vis=True)
    part2(stdscr, vis=True)
