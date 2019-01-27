# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os


for i in os.listdir():
    if not os.path.isfile(i) and not os.path.islink(i):
        print(i)
