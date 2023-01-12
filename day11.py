from __future__ import annotations

import hashlib
import itertools
import re
from abc import ABC
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

def read() -> Dict:
    with open("inputs/day11.txt", mode="+r", encoding="utf-8") as f:
        return f.read()

def tointlist(inp:str) -> List[int]:
    return [ord(c) for c in inp]

def tostr(inp:List[int]) -> str:
    return "".join(chr(c) for c in inp if c != 0)

def increase(inp:List[int], idx:int = 0, inc:int = 1):
    a = ord('a')
    z = ord('z')
    inp[idx] += inc

    while inp[idx] >= z + 1:
        inp[idx] = a + (inp[idx] - z - 1)
        idx += 1
        if idx == len(inp):
            inp.append(a - 1)
        inp[idx] += inc

def increasewithskip(inp:List[int], skippable:List[int]):
    a = ord('a')
    z = ord('z')
    idx = 0

    if inp[idx] + 1 in skippable:
        inp[idx] += 2
    else:
        inp[idx] += 1
    
    while inp[idx] >= z + 1:
        inp[idx] = a + (inp[idx] - z - 1)
        idx += 1
        if idx == len(inp):
            inp.append(a - 1)
        if inp[idx] + 1 in skippable:
            inp[idx] += 2
        else:
            inp[idx] += 1

def c1(inp:List[int]) -> bool:
    for i in range(len(inp) - 2):
        if inp[i] == inp[i+1] + 1 == inp[i+2] + 2:
            return True
    return False

def c2(inp:List[int]) -> bool:
    i, o, l = ord('i'), ord('o'), ord('l')
    return i not in inp and o not in inp and l not in inp

def c3(inp:List[int]) -> bool:
    cnt = idx = 0
    idxs = [None, None]

    while cnt < 2 and idx < len(inp) - 1:
        if inp[idx] == inp[idx+1]:
            idxs[cnt] = idx
            if cnt == 1 and idxs[0] == idxs[1]:
                cnt -= 1
            cnt += 1
            idx += 2
        else:
            idx += 1
    
    return cnt >= 2

def clean_char(inplist:List[int], c:int):
    while c in inplist:
        increase(inplist, inplist.index(c), inc=1)

def nextpwd(inplist:List[int]) -> None:
    ng_letters = list(ord(c) for c in "iol")

    for c in ng_letters:
        clean_char(inplist, c)

    #while not (c1(inplist) and c2(inplist) and c3(inplist)):
    while not (c1(inplist) and c3(inplist)):
        increasewithskip(inplist, ng_letters)
    
def part1():
    inp = read().strip()

    #inp = "hijklmmn"

    inplist = tointlist(inp)
    inplist[:] = inplist[::-1]

    nextpwd(inplist)
    
    print(tostr(inplist[::-1]))

def part2():
    inp = read().strip()

    #inp = "hijklmmn"

    inplist = tointlist(inp)
    inplist[:] = inplist[::-1]

    nextpwd(inplist)
    increase(inplist)
    nextpwd(inplist)
    
    print(tostr(inplist[::-1]))

if __name__ == "__main__":
    part1()
    part2()
