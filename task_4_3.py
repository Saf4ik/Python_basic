# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

A = [x for x in range(-3, 25)]
print(A)
# B = []
# for k in range(len(A)):
#     if A[k] >= 0 and A[k] % 3 == 0 and A[k] % 4 != 0:
#         B.append(k)
# print(B)

print([A[k] for k in range(len(A)) if A[k] >= 0 and A[k] % 3 == 0 and A[k] % 4 != 0])