n = float(input())
rub = int(n // 1)
kop = n * 100 % 100
kop = int(('{0:.0f}'.format(kop)))
print(rub, ' ', kop, sep='')
