# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# 1, 1, 2, 3, 5, 8, 13 ...

print("Задача 1. Ряд Фибоначчи\n", '-' * 23, sep='')

def fibonacci(n, m):
    assert n > 0, 'первый элемент должен быть больше нуля'
    assert m >= n, 'второй элемент должен быть больше первого'

    iFibonacci = 1  # текущее число Фибоначчи по умолчанию
    arrFibonacci = [0] * (m - n + 1)
    goldenRatio = 1.618034  # золотое сечение для формулы Бине
    for i in range(len(arrFibonacci)):
        iFibonacci = int(((goldenRatio ** n) - (1 - goldenRatio) ** n) / (5 ** 0.5))  # формуда Бине
        arrFibonacci[i] = iFibonacci
        n +=1
    return arrFibonacci

print(fibonacci(3, 8), "\n")

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print("Задача 2. 'Пузырьковая' сортировка\n", '-' * 34, sep='')

def sort_to_max(origin_list):
    alter_list = list(origin_list)
    goSort = 1  # проверка отсортирован ли список и нужно ли продолжать сортировку
    while goSort > 0:
        goSort = 0  # проверяем сортировку
        for i in range(len(alter_list)-1):
            if alter_list[i] > alter_list[i + 1]:
                alter_list[i], alter_list[i + 1] = alter_list[i + 1], alter_list[i]
                goSort += 1
    print(origin_list)
    print(alter_list)
    return alter_list

origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(origin_list)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print("\nЗадача 3. Filter\n", '-' * 16, sep='')
def filter_list(origin_list, filter):
    filterList = []
    for i in range(len(origin_list)):
        if origin_list[i] == filter:
            filterList.append(origin_list[i])
    return filterList

origin_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
# print(list(filter(lambda x: x == 4, origin_list)))
print(filter_list(origin_list, 4))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Если координаты середин диагоналей А1А3 и А2А4 совпадают, то параллелограмм
print("\nЗадача 4. Определение фигуры (параллелограмм ли) по координатам\n", '-' * 63, sep='')
def check_parallelogram(a1, a2):
    checkList = list(map(lambda x, y: (x+y)/2, a1, a2))
    return checkList

a1 = [4, 9]
a2 = [3, 12]
a3 = [5, 15]
a4 = [6, 12]
a1a3 = check_parallelogram(a1, a3)
a2a4 = check_parallelogram(a2, a4)
if a1a3 == a2a4:
    print(f"Координаты середин 1-й и 2-й диагонали равны. a1a3 == a2a4: {a1a3}, {a2a4}")
    print("Указанные координаты являются вершинами параллелограмма.")
else:
    print(f"Координаты середин 1-й и 2-й диагонали НЕ равны.  a1a3 != a2a4: {a1a3}, {a2a4}")
    print("Указанные координаты НЕ являются вершинами параллелограмма.")