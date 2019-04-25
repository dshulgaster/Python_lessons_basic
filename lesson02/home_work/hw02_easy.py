import random
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2. банан
# 3. киви
# 4. арбуз

# Подсказка: воспользоваться методом .format()
print("I. Выводим наименование фруктов, используя метод .format:")
fruit = ["яблоко", "банан", "киви", "арбуз"]
print("Вариант 1.\n1. {0:>6} \n2. {1:>6} \n3. {2:>6}\n4. {3:>6}\n".format(fruit[0], fruit[1], fruit[2], fruit[3]))

print(f"Вариант 2 (через f(модно, современно):\n1. {fruit[0]:>6} \n2. {fruit[1]:>6} \n3. {fruit[2]:>6}\n4. {fruit[3]:>6}\n")

print(f"Вариант 3:")
maxLength = 1
for elFruit in fruit:
    if maxLength < len(elFruit):
        maxLength = len(elFruit)
indentFormat = "{:>" + str(maxLength) + "}"
for i in range(len(fruit)):
    # print(str(i+1) + ". " + indentFormat.format(fruit[i]))
    print(f"{i+1}. {fruit[i]:>{maxLength}}")  # PEP 498
print("\n")

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("II. Удалить из первого списка элементы, присутствующие во втором списке.")
list1 = [5, 15, 92, 'hello', False, 3, 'dog']
list2 = [23, 'Jon', 5, 92, 'car', False, 35, 'dog', True]
print("Список 1: {}".format(list1))
print("Список 2: {}".format(list2))

for i1 in list1:
    count = 0
    for i2 in list2:
        if i1 == list2[count]:
            list1.remove(list2[count])
            # print("Дубликат!")
        count += 1

# не совсем верное решение, т.к. это новый список, но оставлю как альтернативное решение
# list3 = []
# for item in set(list1).difference(list2):
#     print(item)
#     list3.append(item)

print("Список 1 после удаления дубликатов: {}\n".format(list1))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("III. НОВЫЙ список из элементов исходного.")
# list4 = [5, 15, 92, 3, 50]
list4 = [random.randint(0, 100) for i in range(15)]
print(f"Исходный список: {list4}")
list5 = []
for i4 in list4:
    if (i4 % 2) == 0:
        list5.append(i4 / 4)
    else:
        list5.append(i4 *2)
print(f"Новый список: {list5}")