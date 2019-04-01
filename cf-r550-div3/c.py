N = int(input())
A = list(map(int, input().split()))
A.sort()
dec = []
inc = []
result = 'YES'
last = None
count = 0
for a in A:
    if a != last:
        inc.append(a)
        last = a
        count = 1
    else:
        if count == 1:
            dec.insert(0, a)
            count += 1
        else:
            result = 'NO'
            break
print(result)
if result == 'YES':
    print(len(inc))
    print(' '.join([str(x) for x in inc]))
    print(len(dec))
    print(' '.join([str(x) for x in dec]))
