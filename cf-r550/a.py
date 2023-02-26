N = int(input())
for _ in range(N):
    string = input()
    alphabet_table = [0] * 26
    result = 'Yes'
    for c in string:
        if alphabet_table[ord(c) - ord('a')] == 1:
            result = 'No'
            break
        else:
            alphabet_table[ord(c) - ord('a')] = 1
    table_string = ''.join([str(x) for x in alphabet_table])
    if len(list(filter(lambda x: x != '', table_string.split('0')))) > 1:
        result = 'No'
    print(result)
