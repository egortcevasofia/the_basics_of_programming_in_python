x = int(input())
y = int(input())
n = 0
while x * 1.1 ** (n - 1) < y:
    n = n + 1
print(n)
