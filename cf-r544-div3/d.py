from collections import Counter
from fractions import Fraction

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
D = []
indef_num = 0
for (a, b) in zip(A, B):
    if a == 0:
        if b == 0:
            indef_num += 1
        continue
    D.append(Fraction(-b, a))

if not D:
    print(indef_num)
else:
    d = Counter(D).most_common()
    print(D.count(d[0][0]) + indef_num)
