# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
'''
split() - разбивает строку на части, используя специальный разделитель
isdigit() - возвращает флаг, указывающий на то, содержит ли строка только цифры
'''
equationSplit = equation.split()    # разбиваем текст на элементы списка
print(equationSplit)
b1 = equationSplit[2]
b1 = int(b1[:-1])   # чуть более длинный вариант: b1 = b1.split('x') -> b1 = int(b1[0])
if equationSplit[3] == "-":
    k = - float(equationSplit[4])
elif equationSplit[3] == "+":
    k = float(equationSplit[4])
y = b1 * x + k
print(f"I. y = -12x + 11111140.2121 = {y} (при х = 2.5)\n")

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

print(f"II. Проверка даты на корректность.")
# date = input("Введите дату в формате:'dd.mm.yyyy'\n")
date = '21.04.2019'
day = month = year = -1 # заранее будем считать дату некорректной, если попытка исключения сработает
daysMonth = {1: 31, 2: 28, 3: 31, 4: 30,
             5: 31, 6: 30, 7: 31,
             8: 31, 9: 30, 10: 31,
             11: 30, 12: 31}
try:
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])
except ValueError:
    day = month = year = "Error"

maxDay = 30
if len(date) == 10 and date.count(".")== 2 and day != "Error":
    if month > 0 and month <=12 and year > 0:
        maxDay = daysMonth[month]
        # print(maxDay)
        if day > 0 and day <= maxDay:
            itsOk = "корректный день"
        else:
            itsOk = "некорректный (день должен быть от 0 до максимума в этом месяце)"
        # itsOk = "корректный (месяц и год соответствуют условию)"
    else:
        if day > 0 and day <= maxDay:
            itsOk = "некорректный (месяц и год не соответствуют условию)"
        else:
            itsOk = "некорректный (месяц и год не соответствуют условию; " \
                    "день должен быть от 0 до до максимума в этом месяце)"
    # print(f" {day}, {month}, {year}")
else:
    itsOk = "некорректный (не соблюдено условие: 2 символа для дня, 2 - для месяца, " \
            "4 - для года; ИЛИ введены символы, отличные от цифр)."

print(f"Формат даты {itsOk}\n")

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

print(f"III. Перевернутая башня.")
floor = 1   # 2 этаж
startRoomThisFloor = 1 #
endRoomThisFloor = 2 #
sumFloors = 10   # sumFloors + 1 = всего этажей (начиная с 0)
roomsThisFloor = []
allRooms = []
lenSquare = 1   # первый квадрат 1*1

# yourRoom = int(input("Введите номер квартиры: \n"))
yourRoom = 5   # 78500000
assert yourRoom <= 2_000_000_000, 'Номер команты слишком большой'

# lastRoom = 1
# lastFloor = 1
# lastRoom = floor * (floor + 1) * (2 * floor +1) / 6    # последняя комната на уровне
# lastFloor = floor * (floor + 1) / 2   # последний этаж на уровне

# tmp = 1817  # всего этажей (вычислил с небольшим запасом по формуле
# print(f"На {tmp} этаже последняя квартира: {int (tmp * (tmp + 1) * (2 * tmp + 1) / 6)}")
sumLevel = 10  # оказалось, что floor == nr :)
roomExp = 7
print(f" Этажей {sumLevel}")
for level in range(sumLevel): # заполняем этажи, всего этажей = sumFloors - 1 !! это уровень, не этаж!!!
    lastFloor = int(level * (level + 1) / 2)  # последний этаж на уровне
    lastRoom = level * (level + 1) * (2 * level + 1) / 6  # последняя комната на уровне
    print(f"lastRoom: {int(lastRoom)}, lastFloor: {lastFloor}, level: {level}")
sumFloors = 10
floor = 1


for nR in range(sumFloors): # заполняем этажи, всего этажей = sumFloors - 1
    floor += 1
    for square in range(0, lenSquare+1):
        roomsThisFloor.clear()
        for i in range(startRoomThisFloor, endRoomThisFloor):   # заполнение комнат, i - конкретная комната
            roomsThisFloor.append(i)
        lenSquare = len(roomsThisFloor)
        startRoomThisFloor = endRoomThisFloor
        endRoomThisFloor = startRoomThisFloor + floor
        allRooms.append(roomsThisFloor[:])
    if nR == sumFloors-1:
        print(f"Всего этажей: {nR+2}")
        print(f"Всего квартир заполнено: {i}")
# print(f"allRooms = {allRooms}")

allBreak = 0
for id1, item in enumerate(allRooms):
    if allBreak == 1:
        break
    for id2, item in enumerate(allRooms[id1]):
        if int(item) == int(yourRoom):
            print(f"этаж {id1+1} слева {id2+1} комната")
            allBreak = 1
            break
