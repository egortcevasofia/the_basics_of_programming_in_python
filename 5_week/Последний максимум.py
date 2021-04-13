a = input().split()
max = int(a[0])
pos = 0
for i in range(len(a)):
    if int(a[i]) >= max:
        max = int(a[i])
        pos = i
print(max, pos)
