
import re
from typing import List, Tuple

Recipe = Tuple[int, int, int, int, int]

def read() -> List[Recipe]:
    recomp = re.compile(
        r"(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)")
    with open("inputs/day15.txt", mode="+r", encoding="utf-8") as f:
        return [
            (int(m[1]), int(m[2]), int(m[3]), int(m[4]), int(m[5]))
            for m in recomp.findall(f.read())
        ]

def eval(status:Recipe, recipes:List[Recipe]):
    sums = [0] * len(recipes[0])
    for i, stat in enumerate(status):
        for j, rec in enumerate(recipes[i]):
            sums[j] += stat*rec
    mults = 1
    for x in sums[:-1]:
        mults *= x if x > 0 else 0
    
    return mults

def eval2(status:Recipe, recipes:List[Recipe]):
    sums = [0] * len(recipes[0])
    for i, stat in enumerate(status):
        for j, rec in enumerate(recipes[i]):
            sums[j] += stat*rec
    mults = 1
    for x in sums[:-1]:
        mults *= x if x > 0 else 0
    
    return mults, sums[-1]

def genTuples(cap, depth):
    if depth == 1:
        yield (cap,)
    else:
        for i in range(1, cap-depth):
            for tail in genTuples(cap-i, depth-1):
                yield (i,) + tail        

def part1():
    inp = read()
    cap = 100
    nrec = len(inp)

    maxv = 0
    for alt in genTuples(cap, nrec):
        maxv = max(maxv, eval(alt, inp))

    print(maxv)

def part2():
    inp = read()
    cap = 100
    nrec = len(inp)

    maxv = 0
    for alt in genTuples(cap, nrec):
        score, cals = eval2(alt, inp)
        if cals == 500:
            maxv = max(maxv, score)

    print(maxv)

if __name__ == "__main__":
    part1()
    part2()
    # for c in generatealt_3(10, 3):
    #     print(c, end=";")
