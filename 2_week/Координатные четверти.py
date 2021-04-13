x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0 and y1 > 0:
    plane1 = 'I'
if x1 < 0 and y1 > 0:
    plane1 = 'II'
if x1 < 0 and y1 < 0:
    plane1 = 'III'
if x1 > 0 and y1 < 0:
    plane1 = 'IV'
if x2 > 0 and y2 > 0:
    plane2 = 'I'
if x2 < 0 and y2 > 0:
    plane2 = 'II'
if x2 < 0 and y2 < 0:
    plane2 = 'III'
if x2 > 0 and y2 < 0:
    plane2 = 'IV'
if plane1 == plane2:
    print('YES')
else:
    print('NO')
