A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if E >= A and D >= B or E >= B and D >= A:
    print('YES')
elif E >= B and D >= C or E >= C and D >= B:
    print('YES')
elif E >= A and D >= C or E >= C and D >= A:
    print('YES')
else:
    print('NO')
