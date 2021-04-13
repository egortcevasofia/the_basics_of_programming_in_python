a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    if b > c:
        print(c, b, a)
    else:
        print(b, c, a)
if b > a and b > c:
    if a > c:
        print(c, a, b)
    else:
        print(a, c, b)
if c > a and c > b:
    if a > b:
        print(b, a, c)
    else:
        print(a, b, c)
if a == b:
    if a > c:
        print(c, a, b)
    else:
        print(a, b, c)
if a == c:
    if a > b:
        print(a, c, b)
    else:
        print(b, a, c)
if b == c:
    if b > a:
        print(a, b, c)
    else:
        print(b, c, a)
