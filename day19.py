from time import sleep
import curses
import itertools
import random
from typing import Dict, List, Set, Tuple, Iterable
from collections import deque

Rule = Tuple[str,str]

uc = "".join(chr(65 + c) for c in range(26))
lc = uc.lower()

def read() -> Tuple[List[Rule], str]:
    replacements = list()
    with open("inputs/day19.txt", mode="+r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=>" in line:
                left, right = line.split(" => ")
                replacements.append((left, right))
        return replacements, line # This is the last line

def getElems(s:str) -> List[str]:
    elems = list()
    for i in range(len(s)):
        if s[i].islower():
            continue
        elif i+1 >= len(s):
            elems.append(s[i])
        elif s[i].isupper() and s[i+1].islower():
            elems.append(s[i:i+2])
        else:
            elems.append(s[i])
    return elems

def read2() -> Tuple[List, List]:
    replacements = list()
    with open("inputs/day19.txt", mode="+r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=>" in line:
                left, right = line.split(" => ")
                replacements.append((left, tuple(getElems(right))))
        return replacements, getElems(line) # This is the last line

def part1(stdscrn, vis=False):
    replacements, startingMolecule = read()
    molecules = set()

    idx = 0
    for origin, target in replacements:
        idx = startingMolecule.find(origin, 0)
        while idx >= 0:
            left = startingMolecule[:idx]
            right = startingMolecule[idx+len(origin):]
            molecules.add(left + target + right)
            if vis:
                stdscr.addstr(0, 0, f"{origin} => {target} @ {idx}\n")
                stdscr.addstr(1, 0, left + target + right)
                stdscr.refresh()
                sleep(1/60)
            idx = startingMolecule.find(origin, idx+1)
    
    print(len(molecules))


def findindices(L:Iterable, K:Iterable):
    indices = list()
    for i in range(len(L)-len(K) + 1):
        found = True
        for j in range(len(K)):
            if L[i + j] != K[j]:
                found = False
                break
        if found:
            indices.append(i)
    return indices

def randomElement(symbols):
    newEl = random.choice(uc) + random.choice(lc)
    while newEl in symbols:
        newEl = random.choice(uc) + random.choice(lc)
    return newEl

def toCNF(rule, symbols):
    newRules = list()
    left, right = rule

    while len(right) > 2:
        newSym = randomElement(symbols)
        symbols.add(newSym)
        newRules.append((left, (right[0], newSym)))
        left = newSym
        right = right[1:]
    newRules.append((left, right))
    return newRules

def part2(stdscrn, vis=False):
    replacements, endingMolecule = read2()
    endingMolecule = tuple(endingMolecule)
    n = len(endingMolecule)

    rules = list()
    symbols = set()
    for x,y in replacements:
        symbols.add(x)
        symbols.update(y)
    orig_symbols = symbols.copy()

    for rule in replacements:
        rules.extend(toCNF(rule, symbols))
    for symb in symbols:
        rules.append((symb, (symb,)))

    memo = [[list() for _ in range(n)] for _ in range(n)]
    #back = [[dict() for _ in range(n)] for _ in range(n)]
    subcounts = [[[] for _ in range(n)] for _ in range(n)]

    for i, a_s in enumerate(endingMolecule):
        for r_l, r_r in rules:
            if len(r_r) == 1 and r_r[0] == a_s:
                memo[0][i].append(r_l)
                subcounts[0][i].append(0)
    
    for length in range(2, n+1):
        for strtspan in range(n - length + 1):
            for partition in range(length - 1):
                mid = strtspan + partition + 1
                lenright = length - partition - 2
                candidates_b = memo[partition][strtspan]
                candidates_c = memo[lenright][mid]
                for Ra, Rb, Rc in [(Ra,) + Rbc for Ra, Rbc in rules if len(Rbc) == 2]:
                    if Rb in candidates_b and Rc in candidates_c:
                        memo[length-1][strtspan].append(Ra)
                        
                        #back[length-1][strtspan].setdefault(Ra, list()).append((partition,Rb,Rc))
                        idx_b = candidates_b.index(Rb)
                        idx_c = candidates_c.index(Rc)
                        
                        subcounts[length-1][strtspan].append(
                            subcounts[partition][strtspan][idx_b] +
                            subcounts[lenright][mid][idx_c] + 
                            (1 if Ra in orig_symbols else 0)
                        )

    print(memo[-1][0])
    print(subcounts[-1][0])


if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    #part1(stdscr, vis=False)
    part2(stdscr, vis=True)
