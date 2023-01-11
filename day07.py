from __future__ import annotations

import hashlib
import itertools
import re
from abc import ABC
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

MAXINT = 65536

def read() -> Dict[str,str]:
    nodeDict = dict()
    with open("inputs/day07.txt", mode="+r", encoding="utf-8") as f:
        for line in f:
            line = line.strip().split(" -> ")
            nodeDict[line[1]] = line[0].split(" ")
    return nodeDict

def process(orig:Dict[str,Any], root:str) -> Dict[str,Any]:
    ops = {
        "AND": lambda x,y: (x & y) % MAXINT,
        "OR": lambda x,y: (x | y) % MAXINT,
        "LSHIFT": lambda x,y: (x << y) % MAXINT,
        "RSHIFT": lambda x,y: (x >> y) % MAXINT,
    }

    nodeDict = orig.copy()
    q = deque()
    q.append(root)

    while len(q) > 0:
        key = q.pop()
        value = nodeDict[key]
        if isinstance(value, int):
            continue
        else:
            q.append(key)
            if len(value) == 1:
                # Direct Assignment
                v = value[0]
                
                if v not in nodeDict:
                    nodeDict[key] = (int(v) if isinstance(v, str) and v.isnumeric() else v)
                else:
                    if isinstance(nodeDict[v], int):
                        nodeDict[key] = nodeDict[v]
                    else:
                        q.append(v)
            elif len(value) == 2:
                # Unary op
                op, v = value
                x = nodeDict[v]
                if isinstance(x, int):
                    nodeDict[key] = (~x) % MAXINT
                else:
                    q.append(v)
            elif len(value) == 3:
                # Binary Op
                left, op, right = value
                x = int(left) if left.isnumeric() else nodeDict[left] 
                y = int(right) if right.isnumeric() else nodeDict[right]
                if isinstance(x, int) and isinstance(y, int):
                    nodeDict[key] = ops[op](x,y)
                elif isinstance(x, int):
                    q.append(right)
                elif isinstance(y, int):
                    q.append(left)
                else:
                    q.append(right)
                    q.append(left)
    
    return nodeDict

def part1():
    nodeDict = read()
    nodeDict = process(nodeDict, "a")
    print(nodeDict["a"])
 
def part2():
    nodeDict = read()
    nodeDict2 = process(nodeDict, "a")

    nodeDict["b"] = nodeDict2["a"]
    nodeDict3 = process(nodeDict, "a")

    print(nodeDict3["a"])

if __name__ == "__main__":
    #part1()
    part2()