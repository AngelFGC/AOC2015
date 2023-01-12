from __future__ import annotations

import hashlib
import itertools
import re
from abc import ABC
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

def read() -> Dict:
    graph = dict()
    with open("inputs/day09.txt", mode="+r", encoding="utf-8") as f:
        for line in f:
            a, _, b, _, dst = line.strip().split(" ")
            graph.setdefault(a, dict())[b] = graph.setdefault(b, dict())[a] = int(dst)
    
    return graph


def part1():
    graph = read()
    keys = list(graph.keys())
    q = deque()
    visited = set()

    min_found = float("inf")

    for k in keys:
    # Node, Distance, Visited
        q.append((k, 0, set()))
        while q:
            node, dist, visited = q.pop()
            if len(visited) == len(keys) - 1:
                min_found = min(min_found, dist)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    v2 = visited.copy()
                    dist2 = dist + graph[node][neighbor]
                    if dist2 <= min_found:
                        v2.add(node)
                        q.append((neighbor, dist2, v2))
    print(min_found)

def part2():
    graph = read()
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
                max_found = max(max_found, dist)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    v2 = visited.copy()
                    dist2 = dist + graph[node][neighbor]
                    v2.add(node)
                    q.append((neighbor, dist2, v2))
    print(max_found)

if __name__ == "__main__":
    #part1()
    part2()
