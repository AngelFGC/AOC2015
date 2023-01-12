from __future__ import annotations

import json
import hashlib
import itertools
import re
from abc import ABC
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

def read() -> Dict:
    with open("inputs/day12.txt", mode="+r", encoding="utf-8") as f:
        return json.loads(f.read().strip())

    
def part1():
    inp = read()
    q = deque()
    q.append(inp)
    s = 0
    while q:
        elem = q.popleft()
        if elem:
            if isinstance(elem, list):
                q.extend(elem)
            elif isinstance(elem, dict):
                q.extend(elem.keys())
                q.extend(elem.values())
            elif isinstance(elem, int):
                s += elem
    print(s)


def part2():
    inp = read()
    q = deque()
    q.append(inp)
    s = 0
    while q:
        elem = q.popleft()
        if elem:
            if isinstance(elem, list):
                q.extend(elem)
            elif isinstance(elem, dict):
                ks, vs = zip(*elem.items())
                if "red" not in vs:
                    q.extend(ks)
                    q.extend(vs)
            elif isinstance(elem, int):
                s += elem
    print(s)


if __name__ == "__main__":
    part1()
    part2()
