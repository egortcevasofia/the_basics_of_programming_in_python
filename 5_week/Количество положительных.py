a = input().split()
count = 0
for i in range(len(a)):
    a[i] = int(a[i])
    if a[i] > 0:
        count += 1
print(count)
