from time import sleep
import curses
import itertools
import math
import random
from typing import Dict, List, Set, Tuple, Iterable
from collections import deque
from functools import cache
from copy import deepcopy

def read() -> List[int]:
    with open("inputs/day25.txt", mode="+r", encoding="utf-8") as f:
        return [int(l.strip()) for l in f]

def gencodes(seed:int, limit:int) -> int:
    for i in range(limit):
        yield i,seed
        seed = (seed*252533) % 33554393

def part1(stdscrn, vis=False):
    #presents = sample()
    row, col = read()
    
    p = row + col - 1
    total_count = p*(p+1) // 2 - row + 1

    row*col + (col**2 - col)//2 + (row**2 - 3*row + 2)//2
    seed = 20151125
    maxy, _ = stdscr.getmaxyx()
    for i,x in gencodes(seed, total_count):
        stdscr.addstr(0, 0, f"Codes - Max: {total_count} | Seed: {seed}\n")
        stdscr.addstr(1 + ((i-1) % (maxy-2)), 0, f"{i}:{x}\n")
        stdscr.refresh()
    stdscr.getch()

    print(x)
    
def part2(stdscrn, vis=False):
    #presents = sample()
    inpt = read()

if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    part1(stdscr, vis=True)
    part2(stdscr, vis=True)
