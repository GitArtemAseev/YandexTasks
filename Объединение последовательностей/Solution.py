x = int(input())
def solution(x):
    A, B, Ax, Bx= 1, 1, 1, 1
    count = 1
    while count <= x:
        if Ax == Bx:
            A += 1
            Ax = A**2
            count -= 1
        elif Ax < Bx:
            Cx = Ax
            A += 1
            Ax = A**2
        else:
            Cx = Bx
            B += 1
            Bx = B**3
        count += 1
    return Cx
print(solution(x))