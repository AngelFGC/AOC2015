from typing import Dict, List, Tuple

import hashlib
import itertools

def read() -> str:
    with open("inputs/day04.txt", mode="+r", encoding="utf-8") as f:
        return f.read().strip()

def part1():
    key = read()
    m = hashlib.md5()
    m.update(bytes(key, encoding="utf-8"))
    for i in itertools.count(1):
        mp = m.copy()
        mp.update(bytes(str(i), encoding="utf-8"))
        d = mp.hexdigest()
        if d[:5] == "0"*5:
            break
    print(i)
 
def part2():
    key = read()
    m = hashlib.md5()
    m.update(bytes(key, encoding="utf-8"))
    for i in itertools.count(1):
        mp = m.copy()
        mp.update(bytes(str(i), encoding="utf-8"))
        d = mp.hexdigest()
        if d[:6] == "0"*6:
            break
    print(i)

if __name__ == "__main__":
    part2()