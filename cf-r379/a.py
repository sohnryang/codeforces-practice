N = int(input())
S = input()
anton = S.count('A')
danik = S.count('D')
if anton == danik:
    print('Friendship')
else:
    print('Anton' if anton > danik else 'Danik')
