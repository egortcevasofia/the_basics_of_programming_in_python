lst = list(map(int, input().split()))
text = []
temp = set()
temp_length = 0
for elem in lst:
    temp.add(elem)
    text.append(('YES' if len(temp) == temp_length else 'NO'))
    temp_length = len(temp)
print(*text, sep="\n")
