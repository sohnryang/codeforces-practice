N = int(input())
even = []
odd = []
A = map(int, input().split())
for a in A:
    if a % 2 == 0:
        even.append(a)
    else:
        odd.append(a)
even.sort()
odd.sort()
if len(even) == len(odd):
    print(0)
elif len(even) > len(odd):
    print(sum(even[:abs(len(odd) - len(even)) - 1]))
else:
    print(sum(odd[:abs(len(odd) - len(even)) - 1]))
