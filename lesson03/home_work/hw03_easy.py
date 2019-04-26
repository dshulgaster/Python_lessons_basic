# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
import math

print("Успел выполнить только задачи Easy - буду догонять!\n")

def my_round(number, ndigits):
    wholeNumber = int(number * 10 ** ndigits) / (10 ** ndigits) # округленное число без учета следующего знака
    addNumberOrchestration = 1 / (10 ** ndigits)    # учесть при округлении следующую цифру
    nextNumeric = (number * 10 ** ndigits - int(number * 10 ** ndigits)) * 10 # следующая цифра после знака округления
    if nextNumeric >= 5:
        finalNumber = wholeNumber + addNumberOrchestration   # итоговое число
    else:
        finalNumber = wholeNumber
    return finalNumber

print("Задача 1. my_round")
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    count = 1 # определим кол-во цифр в числе
    a1_1 = int(ticket_number / 10 ** 5)
    a1_2 = int((ticket_number / 10 ** 5 - int(ticket_number / 10 ** 5)) * 10)
    a1_3 = int((ticket_number / 10 ** 4 - int(ticket_number / 10 ** 4)) * 10)
    sum1 = a1_1 + a1_2 + a1_3
    a2_1 = int((ticket_number / 10 ** 3 - int(ticket_number / 10 ** 3)) * 10)
    a2_2 = int((ticket_number / 10 ** 2 - int(ticket_number / 10 ** 2)) * 10)
    a2_3 = int((ticket_number / 10 ** 1 - int(ticket_number / 10 ** 1)) * 10)
    sum2 = a2_1 + a2_2 + a2_3
    # print(f"{a1_1}, {a1_2}, {a1_3}, {a2_1}, {a2_2}, {a2_3}")
    if len(str(abs(ticket_number))) != 6:
        isLuckyTicket = "Ваш билет не 6-значный, нужен другой билет!"
    else:
        if sum1 == sum2:
            isLuckyTicket = "Билет счастливый!"
        else:
            isLuckyTicket = "Билет НЕсчастливый!"
    return isLuckyTicket

print("\nЗадача 2. lucky_ticket")
print(f"123006: {lucky_ticket(123006)}")
print(f"12321: {lucky_ticket(12321)}")
print(f"436751: {lucky_ticket(436751)}")