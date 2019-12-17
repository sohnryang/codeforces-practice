"""
Codeforces Round #143 (Div. 2) Problem A
https://codeforces.com/contest/231/problem/A
"""

N = int(input())
result = 0
for _ in range(N):
    result += int(sum(map(int, input().split())) >= 2)
print(result)
