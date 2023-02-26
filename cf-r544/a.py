in_time_a = list(map(int, input().split(':')))
in_time_b = list(map(int, input().split(':')))
abs_a = in_time_a[0] * 60 + in_time_a[1]
abs_b = in_time_b[0] * 60 + in_time_b[1]
result = (abs_a + abs_b) // 2
hour = str(result // 60)
if result // 60 < 10:
    hour = '0' + str(result // 60)
minute = str(result % 60)
if result % 60 < 10:
    minute = '0' + str(result % 60)
print('%s:%s' % (hour, minute))
