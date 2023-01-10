
def read() -> str:
    with open("inputs/day01.txt", mode="+r", encoding="utf-8") as f:
        return f.read()

def part1():
    input = read()
    x = y = 0
    for c in input:
        if c == ")":
            x += 1
        elif c == "(":
            y += 1
    print(f"{y - x}")

def part2():
    input = read()
    floor = 0
    for i,c in enumerate(input):
        floor += 1 if c == "(" else -1
        if floor == -1:
            break
    
    print(f"Floor {floor} @ {i+1}")

if __name__ == "__main__":
    part2()