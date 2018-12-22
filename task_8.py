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


""" Вариант решения используя одноменое динамиеское программирование
    Асимтотика O(n).
"""
def fib(n):
    Fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        Fib[i] = Fib[i-1] + Fib[i-2]
    return Fib[n]

n = int(input("Введите целое число: "))
x = fib(n)
print(x)