def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

a = int(input())
b = int(input())
print(a // nod(a, b), b // nod(a, b))
