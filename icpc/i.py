import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

# faster input
LINES = sys.stdin.read().splitlines()[::-1]
def input(): return LINES.pop()

# single integer
inp = lambda: int(input())

# string input
strng = lambda: input().strip()

# words split on white space
strwords = lambda: strng().split()


# string list
strl = lambda: list(input().strip())

# multiple integers, mapped
mul = lambda: map(int,input().strip().split())

# multiple floats, mapped
mulf = lambda: map(float,input().strip().split())

# list of multiple integers
seq = lambda: list(map(int,input().strip().split()))

ceil = lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv = lambda x,d: x//d if(x%d==0) else x//d+1

MOD = 1000000007

mod_add = lambda x, y: ((x % MOD) + (y % MOD)) % MOD
mod_multiply = lambda x, y: ((x % MOD) * (y % MOD)) % MOD
mod_division = lambda x, y: mod_multiply(x, math.pow(y, MOD - 2, MOD))

in_bounds = lambda x, y, grid: x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])

def solve():
    cases = inp()
    
    toppings = set()
    andList = []
    orList = []

    for i in range(cases):
        temp = strwords()
        if len(temp) == 1:
            toppings.add(temp[0])
        else:
            required = temp[-1]
            temp = temp[1:-2]
            tops = []
            for i in range(0, len(temp), 2):
                tops.append(temp[i])
            if 'and' in temp:
                andList.append((tuple(tops), required))
            else:
                orList.append((tuple(tops), required))
    # print(andList)
    # print(orList)
    
    added = 1
    while added != 0:
        added = 0
        
        for ands in andList:
            tops = ands[0]
            required = ands[1]
            if required not in toppings and all([top in toppings for top in tops]):
                toppings.add(required)
                added += 1
        
        for ors in orList:
            tops = ors[0]
            required = ors[1]
            if required not in toppings and any([top in toppings for top in tops]):
                toppings.add(required)
                added += 1
    
    # print(toppings)
    print(len(toppings))
solve()