s = input()
substring = 'f'
pos1 = s.find(substring)
sNext = s[pos1 + 1::1]
pos2 = sNext.find(substring)
if pos1 != -1:
    if pos2 != -1:
        print(pos2 + pos1 + 1)
    elif pos2 == -1:
        print('-1')
elif pos1 == -1:
    print('-2')
