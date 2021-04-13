n = int(input())
sum = 1
while n - 1 != 0 and n > 0:
    sum += n ** 2
    n -= 1
print(sum)
