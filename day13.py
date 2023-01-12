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
    recomp = re.compile(r"(.+) would (.+) (\d+) happiness units by sitting next to (.+).")
    graph:Dict[str,Dict[str,int]] = dict()

    with open("inputs/day13.txt", mode="+r", encoding="utf-8") as f:
        for m in recomp.findall(f.read()):
            a, symb, amnt, b = m[:]
            amnt = (1 if symb == "gain" else -1) * int(amnt)
            if a in graph:
                graph[a][b] = amnt + (graph[a][b] if b in graph[a] else 0)
            else:
                graph[a] = {b:amnt}
            if b in graph:
                graph[b][a] = amnt + (graph[b][a] if a in graph[b] else 0)
            else:
                graph[b] = {a:amnt}

    return graph
    
def part1():
    graph = read()
    #print("\n".join(f"{k}:{inp[k]}" for k in inp))

    keys = list(graph.keys())
    q = deque()
    visited = set()

    max_found = float("-inf")

    for k in keys:
    # Node, Distance, Visited
        q.append((k, 0, set()))
        while q:
            node, dist, visited = q.pop()
            if len(visited) == len(keys) - 1:
                max_found = max(max_found, dist + graph[node][k])
            for neighbor in graph[node]:
                if neighbor not in visited:
                    v2 = visited.copy()
                    dist2 = dist + graph[node][neighbor]
                    v2.add(node)
                    q.append((neighbor, dist2, v2))
    print(max_found)

def part2():
    graph = read()
    #print("\n".join(f"{k}:{inp[k]}" for k in inp))
    
    keys = list(graph.keys())
    graph["YOU"] = dict()
    for k in keys:
        graph["YOU"][k] = 0
        graph[k]["YOU"] = 0
    
    keys.append("YOU")

    q = deque()
    visited = set()

    max_found = float("-inf")

    for k in keys:
    # Node, Distance, Visited
        q.append((k, 0, set()))
        while q:
            node, dist, visited = q.pop()
            if len(visited) == len(keys) - 1:
                max_found = max(max_found, dist + graph[node][k])
            for neighbor in graph[node]:
                if neighbor not in visited:
                    v2 = visited.copy()
                    dist2 = dist + graph[node][neighbor]
                    v2.add(node)
                    q.append((neighbor, dist2, v2))
    print(max_found)


if __name__ == "__main__":
    part1()
    part2()
