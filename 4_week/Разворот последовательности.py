def ret():
    n = int(input())
    if n != 0:
        ret()
        print(n)
    if n == 0:
        print(0)

ret()
