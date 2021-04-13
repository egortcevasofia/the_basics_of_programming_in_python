col1 = int(input())
lin1 = int(input())
col2 = int(input())
lin2 = int(input())
n = col1 - col2
m = lin1 - lin2
if n <= 0:
    n = -n
if m <= 0:
    m = -m
if m + n > 2 or m > 1 or n > 1:
    print('NO')
else:
    print('YES')
