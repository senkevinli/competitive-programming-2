import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br


# faster input
# LINES = sys.stdin.read().splitlines()[::-1]
# def input(): return LINES.pop()

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
    # Implementation goes here.
    pass




primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

results = []

for p in primes:
    print(f'? {p}')
    results.append(strng() == 'yes')


def count(results):
    count = 0
    for r in results:
        if r:
            count += 1
    
    return count

c = count(results)

if c == len(results):
    print('! prime')
    stdout.flush()
    sys.exit(0)

if c > 1:
    print('! composite')
    stdout.flush()
    sys.exit(0)

thing = 0
for i, r in enumerate(results):
    if r:
        thing = i
        break

val = primes[thing]

if val >= 10:
    print('! prime')
    stdout.flush()
    sys.exit(0)

print(f'? {val ** 2}')
result = strng()

if result == 'yes':
    print('! composite')
    stdout.flush()
    sys.exit(0)

print('! prime')
stdout.flush()
sys.exit(0)

