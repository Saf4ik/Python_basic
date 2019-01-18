# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# оставил последовательность в своем обычном виде, надеюсь не критично


def fibonacci(n, m):
    fib = [0, 1] + [0] * (m-1)
    for i in range(2, m+1):
        fib[i] = fib[i-1] + fib[i-2]
    segment_fib = []
    for i in range(n, m+1):
        segment_fib.append(fib[i])
    return segment_fib










