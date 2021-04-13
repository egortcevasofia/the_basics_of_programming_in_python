n = float(input())
wh = int(n / 1)
fr = int(n * 100 % 100)
if fr >= 50:
    wh += 1
print(wh)
