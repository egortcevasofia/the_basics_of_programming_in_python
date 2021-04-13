col1 = int(input())
lin1 = int(input())
col2 = int(input())
lin2 = int(input())
if (col1 + lin1) % 2 == 0:
    color1 = 'dark'
else:
    color1 = 'light'
if (col2 + lin2) % 2 == 0:
    color2 = 'dark'
else:
    color2 = 'light'
if color1 == color2:
    print('YES')
else:
    print('NO')
