a = int(input())
b = int(input())
if a >= b:
    maxim = a
    maxim2 = b
else:
    maxim = b
    maxim2 = a
while a != 0:
    a = int(input())
    if maxim < a:
        maxim2 = maxim
        maxim = a
    elif maxim2 < a:
        maxim2 = a
print(maxim2)
