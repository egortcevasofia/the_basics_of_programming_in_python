A1 = int(input())
B1 = int(input())
C1 = int(input())
A2 = int(input())
B2 = int(input())
C2 = int(input())
if A1 >= B1 and B1 >= C1:
    ab1 = A1
    bb1 = B1
    cb1 = C1
elif A1 >= C1 and B1 <= C1:
    ab1 = A1
    bb1 = C1
    cb1 = B1
elif B1 >= A1 and A1 >= C1:
    ab1 = B1
    bb1 = A1
    cb1 = C1
elif B1 >= C1 and C1 >= A1:
    ab1 = B1
    bb1 = C1
    cb1 = A1
elif C1 >= A1 and A1 >= B1:
    ab1 = C1
    bb1 = A1
    cb1 = B1
elif C1 >= B1 and B1 >= A1:
    ab1 = C1
    bb1 = B1
    cb1 = A1
if A2 >= B2 and B2 >= C2:
    ab2 = A2
    bb2 = B2
    cb2 = C2
elif A2 >= C2 and B2 <= C2:
    ab2 = A2
    bb2 = C2
    cb2 = B2
elif B2 >= A2 and A2 >= C2:
    ab2 = B2
    bb2 = A2
    cb2 = C2
elif B2 >= C2 and C2 >= A2:
    ab2 = B2
    bb2 = C2
    cb2 = A2
elif C2 >= A2 and A2 >= B2:
    ab2 = C2
    bb2 = A2
    cb2 = B2
elif C2 >= B2 and B2 >= A2:
    ab2 = C2
    bb2 = B2
    cb2 = A2
if ab1 == ab2 and bb1 == bb2 and cb1 == cb2:
    print('Boxes are equal')
elif ab1 <= ab2 and bb1 <= bb2 and cb1 <= cb2:
    print('The first box is smaller than the second one')
elif ab1 >= ab2 and bb1 >= bb2 and cb1 >= cb2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
