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

def prefix_sum(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    return arr


def solve():
    peeps, chairs = mul()
    arr = seq()
    if chairs <= peeps:
        return False
    
    leftover = chairs - peeps
    
    arr.sort(reverse=True)
    
    left = right = 0
    idx = 0
    
    fill_left = True
    while idx < len(arr):

        if idx == 0:
            left = arr[idx]
            right = arr[idx]
            
            leftover -= left
            leftover -= right
            idx += 1
            continue
        
        cur = arr[idx]
        
        if fill_left:
            left = cur
            leftover -= left
            fill_left = False
        else:
            right = cur
            leftover -= right
            fill_left = True
            
        idx += 1
    
    leftover += min(left, right)
    
    return leftover >= 0
        
    

cases = inp()
for _ in range(cases):
    print('YES' if solve() else 'NO')