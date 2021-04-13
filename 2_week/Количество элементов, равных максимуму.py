a = int(input())
maxim = a
k = 1
while a != 0:
    a = int(input())
    if a > maxim:
        k = 0
        maxim = a
    if a == maxim:
        k += 1
print(k)
