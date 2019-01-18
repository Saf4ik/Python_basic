# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter_func(func, sequence):
    output = []
    for i in range(len(sequence)):
        if func(sequence[i]):
            output.append(sequence[i])
    return output


func = lambda x: type(x) == str
list = [1, 15, "q", "e", 32, "dsa"]
print(filter_func(func, list))










