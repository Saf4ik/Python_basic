# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    a = list(str(ticket_number))
    if len(a) == 6:
        b = int(a[0]) + int(a[1]) + int(a[2])
        c = int(a[3]) + int(a[4]) + int(a[5])
        if b == c:
            return "Yes"
    return "No"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(123106))