
import re
from typing import List, Tuple

def read():
    recomp = re.compile(
        r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")
    with open("inputs/day16.txt", mode="+r", encoding="utf-8") as f:
        return {
            int(m[0]):{
                m[1]:int(m[2]),
                m[3]:int(m[4]),
                m[5]:int(m[6])
            }
            for m in recomp.findall(f.read())
        }

def part1():
    inpt = read()
    
    mfcsam_res = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    todel = set()
    for auntid, auntdict in inpt.items():
        for k in auntdict:
            if mfcsam_res[k] != auntdict[k]:
                todel.add((auntid, k))
    
    for a,k in todel:
        del inpt[a][k]

    print([auntid for auntid, auntdict in inpt.items() if len(auntdict) > 2])

def part2():
    inpt = read()
    
    mfcsam_res = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    lowerbounds = {"cats", "trees"}
    upperbounds = {"pomeranians", "goldfish"}
    alts = lowerbounds.union(upperbounds)

    todel = set()
    for auntid, auntdict in inpt.items():
        for k in auntdict:
            if not (
                (k in lowerbounds and mfcsam_res[k] < auntdict[k]) or
                (k in upperbounds and mfcsam_res[k] > auntdict[k]) or
                (k not in alts and mfcsam_res[k] == auntdict[k])
            ):
                todel.add((auntid, k))
    
    for a,k in todel:
        del inpt[a][k]

    print([auntid for auntid, auntdict in inpt.items() if len(auntdict) > 2])

if __name__ == "__main__":
    part1()
    part2()
