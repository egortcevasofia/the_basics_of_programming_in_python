def sum(i):
    global ch
    if i != 0:
        i -= 1
        ch += 1
        sum(i)
    return ch

a = int(input())
b = int(input())
ch = 0
sum(a)
sum(b)
print(ch)
