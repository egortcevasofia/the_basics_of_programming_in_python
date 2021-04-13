n = int(input())
s = list(map(int, input().split(" ")))
x = int(input())
ass = []
for i in range(n):
    s[i] = int(s[i])
    ass.append(abs(s[i] - x))
n = ass.index(min(ass))
print(s[n])
