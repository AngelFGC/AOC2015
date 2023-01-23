from time import sleep
import curses
import itertools
import math
import random
from typing import Dict, List, Set, Tuple, Iterable
from collections import deque
from functools import cache
from copy import deepcopy

sample = """inc a
jio a, +2
tpl a
inc a"""

Instruction = Tuple[str, Tuple]

class TuringMachine(object):
    code:List[Instruction]
    ppointer:int
    regs:Dict[str,int]
    def __init__(self, instrs:List[str]) -> None:
        self.regs = dict()
        self.code = list()
        self.ppointer = self.regs["a"] = self.regs["b"] = 0
        for instr in instrs:
            left, right = instr.split(" ", maxsplit=1)
            self.code.append((
                left,
                tuple(c.strip() for c in right.split(","))
            ))
    
    @property
    def regA(self) -> int:
        return self.regs["a"]
    
    @regA.setter
    def regA(self, newV:int):
        self.regs["a"] = newV

    @property
    def regB(self) -> int:
        return self.regs["b"]
    
    @regB.setter
    def regB(self, newV:int) -> None:
        self.regs["b"] = newV

    def halted(self) -> bool:
        return not (0 <= self.ppointer < len(self.code))

    def executeNext(self) -> bool:
        if not self.halted():
            instr, data = self.code[self.ppointer]
            nextPtr = self.ppointer + 1

            if len(data) == 1:
                reg = data[0]
                if instr == "hlf":
                    self.regs[reg] = self.regs[reg] // 2
                elif instr == "tpl":
                    self.regs[reg] *= 3
                elif instr == "inc":
                    self.regs[reg] += 1
                elif instr == "jmp":
                    offset = int(reg)
                    nextPtr = self.ppointer + offset
                else:
                    print(instr)
            else:
                r, offset = data
                offset = int(offset)
                if instr == "jie" and self.regs[r] % 2 == 0:
                    nextPtr = self.ppointer + offset
                elif instr == "jio"  and self.regs[r] == 1:
                    nextPtr = self.ppointer + offset
                elif instr not in ["jie", "jio"]:
                    print(instr)
            
            self.ppointer = nextPtr
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"i:{self.ppointer}|a:{self.regA}|b:{self.regB}"
    
    def __str__(self) -> str:
        return (
            f"PC: {self.ppointer}\n" + 
            (
                f"Next: {self.code[self.ppointer]}\n" 
                if 0 <= self.ppointer < len(self.code)
                else "Next: ----\n"
            ) + 
            f"Registry A: {self.regA}\n" +
            f"Registry B: {self.regB}\n"
        )


def read():    
    with open("inputs/day23.txt", mode="+r", encoding="utf-8") as f:
        return [l.strip() for l in f]


def printMachine(stdscrn, m:TuringMachine, wait:bool=False) -> None:
    # stdscr.addstr(y, x, "#")
    # sleep(1/60)
    m_data = str(m)
    stdscr.addstr(0,0, "***********************\n")
    stdscr.addstr(1,0, "*  LE TURING MACHINE  *\n")
    stdscr.addstr(2,0, "***********************\n")
    for i,line in enumerate(m_data.splitlines(keepends=True)):
        stdscr.addstr(i+3,0, line)
    if m.halted():
        stdscr.addstr(i+4,0, "==HALTED==\n")
        stdscr.refresh()
        stdscr.getch()
    elif wait:
        stdscr.refresh()
        #stdscr.getch()
        #sleep(0.5)
        sleep(1/60)
    

def part1(stdscrn, vis=False):
    code =  read()
    #code = sample.splitlines()
    M = TuringMachine(code)
    printMachine(stdscrn, M, wait=vis)
    while M.executeNext():
        printMachine(stdscrn, M, wait=vis)
    printMachine(stdscrn, M, wait=vis)
    
def part2(stdscrn, vis=False):
    code =  read()
    #code = sample.splitlines()
    M = TuringMachine(code)
    M.regA = 1
    printMachine(stdscrn, M, wait=vis)
    while M.executeNext():
        printMachine(stdscrn, M, wait=vis)
    printMachine(stdscrn, M, wait=vis)

if __name__ == "__main__":
    # CURSES
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    if curses.has_colors():
        curses.start_color()
    
    #part1(stdscr, vis=True)
    part2(stdscr, vis=True)
