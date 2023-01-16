
import curses
import itertools
from typing import List, Set, Tuple

Light = Tuple[int, int]

def read() -> Tuple[Set[Light], Light, Light]:
    lights = set()
    with open("inputs/day18.txt", mode="+r", encoding="utf-8") as f:
        for y, line in enumerate(f.readlines()):
            for x, c in enumerate(line.strip()):
                if c == "#":
                    lights.add((x,y))
    return lights, (0,0), (x,y)

def getNeighbors(curr:Light, lb:Light, ub:Light) -> Set[Light]:
    return set(
        (curr[0] + x, curr[1] + y) for x,y in itertools.product((-1,0,1), repeat=2)
        if not(x == y == 0) and 
            lb[0] <= curr[0] + x <= ub[0] and 
            lb[1] <= curr[1] + y <= ub[1]
    )

def getNextState(currState:Set[Light], lb:Light, ub:Light):
    nextState = set()
    itor = itertools.product(
        range(lb[0], ub[0] + 1), range(lb[1], ub[1] + 1)
    )
    for x, y in itor:
        neighbors = getNeighbors((x,y), lb, ub)
        lit_neighbors = currState.intersection(neighbors)
        if (x,y) in currState:
            if 2 <= len(lit_neighbors) <= 3:
                nextState.add((x,y))
        else:
            if len(lit_neighbors) == 3:
                nextState.add((x,y))
    return nextState

def printstate(stdscr, state:Set[Light], lb:Light, ub:Light):
    itor = itertools.product(
        range(lb[0], ub[0] + 1), range(lb[1], ub[1] + 1)
    )
    for x, y in itor:
        if (x,y) in state:
            stdscr.addstr(y, x, "#")
        else:
            stdscr.addstr(y, x, ".")
    stdscr.refresh()
    stdscr.getch()

def part1(stdscrn):
    inpt, lb, ub = read()
    state = inpt
    #printstate(stdscrn, state, lb, ub)
    for _ in range(100):
        state = getNextState(state, lb, ub)
        #printstate(stdscrn, state, lb, ub)
    
    print(len(state))
    
def part2(stdscrn):
    inpt, lb, ub = read()
    state = inpt
    bdrs_x, bdrs_y = tuple(zip(lb,ub))
    corners = set((x,y) for x,y in itertools.product(bdrs_x, bdrs_y))
    state.update(corners)
    #printstate(stdscrn, state, lb, ub)
    for _ in range(100):
        state = getNextState(state, lb, ub)
        state.update(corners)
        #printstate(stdscrn, state, lb, ub)
    
    print(len(state))

if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    part1(stdscr)
    
    part2(stdscr)
