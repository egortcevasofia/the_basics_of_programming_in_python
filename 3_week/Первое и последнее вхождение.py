s = input()
substring = 'f'
n = len(s)
sExch = s[::-1]
pos1 = s.find(substring)
pos2 = sExch.find(substring)
headPos = n - pos2 - 1
if pos1 != -1:
    if headPos == pos1:
        print(pos1)
    elif headPos != pos1:
        print(pos1, headPos)
