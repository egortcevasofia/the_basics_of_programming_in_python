a = int(input())
b = int(input())
c = int(input())
if a > b and a > c and c != b:
    if b > c:
        print(c, b, a)
    else:
        print(b, c, a)
if b > a and b > c and c != a:
    if a > c:
        print(c, a, b)
    else:
        print(a, c, b)
if c > a and c > b and a != b:
    if a > b:
        print(b, a, c)
    else:
        print(a, b, c)
if a == b and a != c:
    if a > c:
        print(c, a, b)
    else:
        print(a, b, c)
if a == c and a != b:
    if a > b:
        print(b, a, c)
    else:
        print(a, c, b)
if b == c and b != a:
    if b > a:
        print(a, b, c)
    else:
        print(b, c, a)
if a == b == c:
    print(a, b, c)
