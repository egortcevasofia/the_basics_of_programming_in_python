n = int(input())
m = int(input())
k = int(input())
if (k % m == 0 or k % n == 0) and (n * m > k):
    print('YES')
else:
    print('NO')
