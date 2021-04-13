n = int(input())
x = n
nod = n
while x > 1:
    if n % x == 0:
        nod = x
    x = x - 1
print(nod)
