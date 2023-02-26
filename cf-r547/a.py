[N, M] = map(int, input().split())
if N == M:
    print(0)
else:
    div = M // N
    if (N * div) != M:
        print(-1)
    else:
        result = 0
        while div != 1:
            if div % 2 == 0:
                result += 1
                div /= 2
                continue
            elif div % 3 == 0:
                result += 1
                div /= 3
                continue
            else:
                result = -1
                break
        print(result)
