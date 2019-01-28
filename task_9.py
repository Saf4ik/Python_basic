""" Задание-3
    Вывести на экран:
    AAABBBAAABBBAAABBB
    BBBAAABBBAAABBBAAA
    AAABBBAAABBBAAABBB
    (таких строк n, в каждой строке m троек AAA)
"""


n = int(input("Количество строк: "))
m = int(input("Количество троек ААА: "))


for i in range(n):
    if i % 2 == 0:
        print("AAABBB" * m)
    else:
        print("BBBAAA" * m)