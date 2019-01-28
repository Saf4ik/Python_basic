# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def parallelogram(A, B, C, D):
    mid_diag_1 = [(A[0] + C[0]) / 2, (A[1] + C[1]) / 2]
    mid_diag_2 = [(B[0] + D[0]) / 2, (B[1] + D[1]) / 2]
    if mid_diag_1 == mid_diag_2:
        return True
    return False


A1 = [0, 0]
A2 = [5, 10]
A3 = [20, 10]
A4 = [15, 0]
x = parallelogram(A1, A2, A3, A4)
print(x)









# if (y1 == y4) and (y2 == y3) and (abs(x1-x2) == abs(x3-x4))
