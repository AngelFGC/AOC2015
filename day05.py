from typing import Dict, List, Tuple

import hashlib
import itertools
import re

def read() -> str:
    with open("inputs/day05.txt", mode="+r", encoding="utf-8") as f:
        return [l.strip() for l in f]

def part1():
    words = read()
    rule1 = re.compile(r"[aeiou]")
    rule2 = re.compile(r"(\S)\1")
    rule3 = re.compile(r"ab|cd|pq|xy")

    r1 = lambda w: len(rule1.findall(w)) >= 3
    r2 = lambda w: rule2.search(w) is not None
    r3 = lambda w: rule3.search(w) is None

    print(sum(r1(w) * r2(w) * r3(w) for w in words))
 
def part2():
    words = read()
    rule1 = re.compile(r"(\S\S).*(\1)")
    rule2 = re.compile(r"(\S)\S(\1)")

    r1 = lambda w: rule1.search(w) is not None
    r2 = lambda w: rule2.search(w) is not None
    

    print(sum(r1(w) * r2(w) for w in words))

if __name__ == "__main__":
    part1()
    part2()