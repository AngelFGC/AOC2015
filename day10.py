from __future__ import annotations

import hashlib
import itertools
import re
from abc import ABC
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

def read() -> Dict:
    with open("inputs/day10.txt", mode="+r", encoding="utf-8") as f:
        return f.read()

def looknsay(look:str):
    return "".join(
        str(len(m[0])) + m[0][0]
        for m in re.finditer(r"(1{1,3}|2{1,3}|3{1,3})", look)
    )

def part1():
    inp = read()
    for i in range(40):
        inp = looknsay(inp)
    
    print(len(inp))

def part2():
    inp = read()
    for i in range(50):
        inp = looknsay(inp)
    
    print(len(inp))

if __name__ == "__main__":
    #part1()
    part2()
