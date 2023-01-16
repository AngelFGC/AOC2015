from typing import List

def read():
   with open("inputs/day17.txt", mode="+r", encoding="utf-8") as f:
        return [int(line.strip()) for line in f]

def knapsack01(idx:int, amnt:int, items:List[int], cap:int):
    if (idx >= len(items) and amnt < cap) or amnt > cap:
        return 0
    elif amnt == cap:
        return 1
    else:
        notchosen = knapsack01(idx + 1, amnt, items, cap)
        chosen = knapsack01(idx + 1, amnt + items[idx], items, cap)
        return chosen + notchosen

def knapsack01_p2_search(idx:int, amnt:int, items:List[int], cap:int, chosen:int):
    if (idx >= len(items) and amnt < cap) or amnt > cap:
        return 0, 0
    elif amnt == cap:
        return 1, chosen
    else:
        notchosen, chosen_amnt1 = knapsack01_p2_search(idx + 1, amnt, items, cap, chosen)
        chosen, chosen_amnt2 = knapsack01_p2_search(idx + 1, amnt + items[idx], items, cap, chosen + 1)

        amnt = (chosen_amnt1 if chosen_amnt2 == 0 else
                chosen_amnt2 if chosen_amnt1 == 0 else 
                min(chosen_amnt1, chosen_amnt2))

        return chosen + notchosen, amnt

def knapsack01_p2_choice(idx:int, amnt:int, items:List[int], cap:int, chosen:int, chosencap:int):
    if amnt == cap and chosen == chosencap:
        return 1
    elif chosen >= chosencap or amnt >= cap or idx >= len(items):
        return 0
    else:
        notchosen = knapsack01_p2_choice(idx + 1, amnt, items, cap, chosen, chosencap)
        chosen = knapsack01_p2_choice(idx + 1, amnt + items[idx], items, cap, chosen + 1, chosencap)
        return chosen + notchosen

def part1():
    NOG = 150
    inpt = read()

    print(knapsack01(0, 0, inpt, NOG))
    
def part2():
    NOG = 150
    inpt = read()

    _, minimum = knapsack01_p2_search(0, 0, inpt, NOG, 0)
    print(minimum)
    print(knapsack01_p2_choice(0, 0, inpt, NOG, 0, minimum))

if __name__ == "__main__":
    part1()
    print("-"*10)
    part2()
