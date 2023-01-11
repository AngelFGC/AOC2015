from typing import Dict, List, Tuple

import hashlib
import itertools
import re

def read() -> str:
    extractor = re.compile(r"^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$", flags=re.MULTILINE)
    output = list()
    with open("inputs/day06.txt", mode="+r", encoding="utf-8") as f:
        for line in f:
            m = extractor.match(line)
            if m is not None:
                groups = m.groups()
                output.append(tuple(
                    g if i == 0 else int(g)
                    for i, g in enumerate(groups)
                ))
    return output

def part1():
    instr = read()
    lights = set() # Only register the LIGHTS that are ON

    for action, x1, y1, x2, y2 in instr:
        for x,y in itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)):
            if action == "turn on" and (x,y) not in lights:
                lights.add((x,y))
            elif action == "turn off" and (x,y) in lights:
                lights.remove((x,y))
            elif action == "toggle":
                if (x,y) in lights:
                    lights.remove((x,y))
                else:
                    lights.add((x,y))
    
    print(len(lights))
 
def part2():
    instr = read()
    lights = dict()

    for action, x1, y1, x2, y2 in instr:
        for x,y in itertools.product(range(x1, x2 + 1), range(y1, y2 + 1)):
            if action == "turn on":
                lights[(x,y)] = lights.setdefault((x,y), 0) + 1
            elif action == "turn off":
                lights[(x,y)] = max(lights.setdefault((x,y), 0) - 1, 0)
            else:
                lights[(x,y)] = lights.setdefault((x,y), 0) + 2
    
    print(sum(lights[k] for k in lights))

if __name__ == "__main__":
    #part1()
    part2()