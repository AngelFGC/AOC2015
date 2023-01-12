from __future__ import annotations

import hashlib
import itertools
import re
from abc import ABC
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple


def read():
    with open("inputs/day08.txt", mode="+r", encoding="utf-8") as f:
        return [line.strip() for line in f]


def part1():
    strings = read()
    sumlens = 0

    for line in strings:
        c = eval(line)
        sumlens += len(line) - len(c)
        #print(f"{len(line):3d}:{len(c):3d} \t {line} --> {c}")

    print(sumlens)


def part2():
    strings = read()
    sumlens = 0

    for line in strings:
        c = repr(line).replace('"', r'\"')
        sumlens += len(c) - len(line) 
        #print(f"{len(line):3d}:{len(c):3d} \t {line} --> {c}")

    print(sumlens)

if __name__ == "__main__":
    # part1()
    part2()
