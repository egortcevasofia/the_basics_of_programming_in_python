s = input()
c = s.count(' ')
if len(s) == c:
    print(0)
if c == 1 and len(s) == 2:
    print(1)
else:
    print(c + 1)
