from typing import List, Tuple

BoxDim = Tuple[int, int, int]

def read() -> List[BoxDim]:
    with open("inputs/day02.txt", mode="+r", encoding="utf-8") as f:
        return [tuple(map(lambda x: int(x),l.strip().split("x"))) for l in f]

def area(l:int, w:int, h:int) -> int:
    lw, wh, hl = l*w, w*h,  h*l
    return 2*(lw + wh + hl) + min(lw, wh, hl)

def ribbons(l:int, w:int, h:int) -> int:

    return 2*min(l+w, w+h, h+l) + l*w*h

def part1():
    boxes = read()
    #boxes = [(2,3,4),(1,1,10)]

    print(sum(area(l,w,h) for l,w,h in boxes))

def part2():
    boxes = read()
    #boxes = [(2,3,4),(1,1,10)]

    print(sum(ribbons(l,w,h) for l,w,h in boxes))

if __name__ == "__main__":
    part2()