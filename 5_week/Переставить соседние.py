s = list(map(int, input().split(" ")))
ans = []
ben = []
for i in range(len(s)):
    while i < len(s) - 1 and len(ans) < len(s):
        ans.append(s[i + 1])
        ans.append(s[i])
        i += 2
    if len(s) % 2 != 0:
        ben.append(s.pop())
        r = ben[0]
        ans.append(r)
print(*ans)
