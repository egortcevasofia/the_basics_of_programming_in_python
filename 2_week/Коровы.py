n = int(input())
x = n % 10
y = n % 100
if x == 0 or 11 <= y <= 14 or 5 <= x <= 9:
    print(n, 'korov')
if x == 1 and y != 11 and y != 12 and y != 13 and y != 14:
    print(n, 'korova')
if 2 <= x <= 4 and y != 11 and y != 12 and y != 13 and y != 14:
    print(n, 'korovy')
