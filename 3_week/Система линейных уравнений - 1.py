a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
det = a * d - c * b
detX = e * d - f * b
detY = a * f - c * e
x = detX / det
y = detY / det
print(x, y)
