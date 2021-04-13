s = input()
substring = 'h'
n = len(s)
sExch = s[::-1]
pos1 = s.find(substring)
pos2 = sExch.find(substring)
headPos = n - pos2 - 1
print(s[0:pos1], s[headPos + 1:], sep='')
