n = int(input())
m = int(input())
k = int(input())
if n != m and n != k and n > m and n > k:
    print(n)
if m != n and m != k and m > n and m > k:
    print(m)
if k != n and k != m and k > n and k > m:
    print(k)
if n == m and n > k:
    print(n)
if n == k and n > m:
    print(n)
if m == k and m > n:
    print(m)
if n == m == k:
    print(n)
