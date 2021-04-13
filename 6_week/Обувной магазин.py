n = int(input())
s = list(map(int, input().split(" ")))
help = []
count = 1
if n <= 100 and max(s) <= 100:
    for i in range(0, len(s)):
        if s[i] >= n:
            help.append(s[i])
    for j in range(0, len(help)):
        if (int(help[j]) - int(help[j - 1])) >= 3:
            count += 1
print(count)
