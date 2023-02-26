import itertools
from math import gcd
from sys import stdin

infast = lambda: stdin.readline().strip()

T = int(infast())
for _ in range(T):
    N = int(infast())
    A = [int(x) for x in infast().split()]
    for x, y in itertools.combinations(A, 2):
        if gcd(x, y) <= 2:
            print("Yes")
            break
    else:
        print("No")
