from sys import stdin

infast = lambda: stdin.readline().strip()

T = int(infast())
for _ in range(T):
    N = int(infast())
    A = [int(x) for x in infast()]
    mid = N // 2
    diffs = [x ^ y for x, y in zip(A[:mid], A[-1 : -mid - 1 : -1])]
    one_appeared = False
    zero_appeard = False
    for diff in diffs:
        if diff == 1:
            if one_appeared and zero_appeard:
                print("No")
                break
            one_appeared = True
        else:
            if one_appeared:
                zero_appeard = True
    else:
        print("Yes")
