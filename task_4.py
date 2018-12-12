""" Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
    Например, дается x = 58375.
    Нужно вывести максимальную цифру в данном числе, т.е. 8.
    Подразумевается, что мы не знаем это число заранее.
    Число приходит в виде целого беззнакового.
"""


a = int(input("Введите число: "))
max = 0
while a > 10:
    x = a % 10
    a //= 10
    if x > max:
        max = x
print(max)