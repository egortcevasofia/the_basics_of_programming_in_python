a = input().split()
b = []
for i in range(len(a)):
    if int(a[i]) > int(a[i - 1]):
        if i > 0:
            b.append(a[i])
print(' '.join(map(str, b)))
