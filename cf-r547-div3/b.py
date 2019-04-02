N = int(input())
A = list(map(int, input().split()))

optimal = 0

if A[0] == 1 and A[-1] == 1:
    leading = 0
    ending = 0
    for i in range(N):
        if A[i] == 1:
            leading += 1
        else:
            break
    for i in range(N - 1, -1, -1):
        if A[i] == 1:
            ending += 1
        else:
            break
    optimal = leading + ending

current = 0
for a in A:
    if a == 0:
        optimal = max(optimal, current)
        current = 0
    else:
        current += 1
optimal = max(optimal, current)

print(optimal)
