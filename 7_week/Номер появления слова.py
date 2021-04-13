fin = open("input.txt")
myDict = {}
checker = list()
for line in fin:
    words = line.split()
    i = 0
    for word in words:
        if word not in myDict:
            myDict[word.strip()] = 1
            checker.append(0)
        else:
            myDict[word.strip()] = myDict[word.strip()] + 1
            checker.append(myDict[word.strip()] - 1)
print(*checker)
