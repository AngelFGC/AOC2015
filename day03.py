from typing import Dict, List, Tuple

def read() -> str:
    with open("inputs/day03.txt", mode="+r", encoding="utf-8") as f:
        return f.read().strip()

def part1():
    start = (0,0)
    visited = {start:1}
    (x,y) = start
    dirs = {
        "^":(0,-1),
        ">":(1,0),
        "<":(-1,0),
        "v":(0,1)
    }
    input = read()
    for c in input:
        dx,dy = dirs[c]
        x += dx
        y += dy
        updatevisited(x, y, visited)
    
    print(len(visited))

def updatevisited(x:int, y:int, visited:Dict):
    if (x,y) in visited:
        visited[(x,y)] += 1
    else:
        visited[(x,y)] = 1
 
def part2():
    start = (0,0)
    visited = {start:1}
    (xs,ys) = start
    (xr,yr) = start
    dirs = {
        "^":(0,-1),
        ">":(1,0),
        "<":(-1,0),
        "v":(0,1)
    }
    input = read()
    for i,c in enumerate(input):
        dx,dy = dirs[c]
        if i % 2==0:
            xs += dx
            ys += dy
            updatevisited(xs, ys, visited)
        else:
            xr += dx
            yr += dy
            updatevisited(xr, yr, visited)
    
    print(len(visited))

if __name__ == "__main__":
    part2()