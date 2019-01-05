# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


A = ["apple", "mango", "orange", "grape", "apricot"]
B = ["pineapple", "kivi", "orange", "cherry", "grape"]

print([A[i] for i in range(len(A)) for j in range(len(B)) if A[i] == B[j]])

# C = []
# for i in range(len(A)):
#     for j in range(len(B)):
#         if A[i] == B[j]:
#             C.append(A[i])
#
# print(C)

