from collections import defaultdict
from sys import stdin
from typing import DefaultDict, Dict

infast = lambda: stdin.readline().strip()

T = int(infast())

for _ in range(T):
    N, M = map(int, infast().split())
    A = [int(x) for x in infast().split()]
    last_seen: Dict[int, int] = {}
    count: DefaultDict[int, int] = defaultdict(lambda: 0)
    for a in A:
        last_seen[a] = 0
    for i in range(1, M + 1):
        P, V = map(int, infast().split())
        old_val = A[P - 1]
        count[old_val] += i - last_seen[old_val]
        del last_seen[old_val]
        A[P - 1] = V
        last_seen[V] = i
    for k, v in last_seen.items():
        count[k] += M - v + 1
    res = 0
    for c in count.values():
        res += M * (M + 1) // 2 - (M - c) * (M - c + 1) // 2
    print(res)
