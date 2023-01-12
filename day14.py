from __future__ import annotations

import json
import hashlib
import itertools
import re
from abc import ABC
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

Reindeer = Tuple[str, int, int , int]

def read() -> List[Reindeer]:
    recomp = re.compile(r"(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
    with open("inputs/day14.txt", mode="+r", encoding="utf-8") as f:
        return [
            (m[0], int(m[1]), int(m[2]), int(m[3]))
            for m in recomp.findall(f.read())
        ]
    
def part1():
    inp = read()
    total_time = 2503
    dists = list()

    for name, speed, time, rest in inp:
        segment_distance = speed * time
        segment_time = time + rest
        segment_count = total_time // segment_time
        segment_remain_time = total_time % segment_time
        segment_remain_distance = speed * min(segment_remain_time, time)
        distance_covered = segment_distance * segment_count + segment_remain_distance
        dists.append((distance_covered, name))

    dists.sort()

    print(dists)
    print(dists[-1])


@dataclass(eq=True,order=True)
class Reindeer(object):
    name:str = field(compare=False)
    speed:int = field(compare=False, repr=False)
    time:int = field(compare=False, repr=False)
    rest:int = field(compare=False, repr=False)
    distance:int = field(init=False, compare=True, default=0)
    timerun:int = field(init=False, compare=False, default=0)
    points:int = field(init=False, compare=False, default=0)

    def update(self):
        self.timerun += 1
        time_in_block = self.timerun % (self.time + self.rest)
        if time_in_block < self.time:
            self.distance += self.speed

def part2():
    inp = read()
    total_time = 2503
    reindeers = [Reindeer(n,s,t,r) for n,s,t,r in inp]

    for _ in range(total_time):
        for rdeer in reindeers:
            rdeer.update()
        reindeers.sort()
        reindeers[-1].points += 1
    
    reindeers.sort(key=lambda r: r.points)
    print(reindeers)


if __name__ == "__main__":
    part1()
    part2()
