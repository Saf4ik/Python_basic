""" Задание-2
    Найдите n-ое число Фибоначчи
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


n = int(input("Введите целое число: "))
x = fib(n)
print(x)