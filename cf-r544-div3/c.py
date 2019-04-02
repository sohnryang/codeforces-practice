N = int(input())
A = list(map(int, input().split()))
A.sort()
lo = 0
a_table = dict()
for a in A:
    if a not in a_table:
        a_table[a] = 1
    else:
        a_table[a] += 1

optimal = 0
for (key, val) in a_table.items():
    result = 0
    for i in range(key, key + 6):
        if i in a_table:
            result += a_table[i]
    optimal = max(optimal, result)
print(optimal)
