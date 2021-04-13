b, keys, words = [], [], []
for i in range(int(input())):
    b.append(list(input().split()))
for i in range(len(b)):
    keys.append(b[i][1])
    words.append(b[i][0])
slov = dict(zip(words, keys))
slov1 = dict(zip(keys, words))
req = input()
if req in slov.keys():
    print(slov.get(req))
if req in slov1.keys():
    print(slov1.get(req))
