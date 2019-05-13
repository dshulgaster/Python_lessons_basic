# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

print(f"Задача-1. Написать класс для треугольника, заданного по 3-м точкам\n")

class Triangle:
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.XY12 = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)
        self.XY13 = round(((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5, 2)
        self.XY23 = round(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5, 2)

    @property
    def perimeter(self):
        self.perimeterTreangle = self.XY12 + self.XY13 + self.XY23
        return round(self.perimeterTreangle, 2)

    @property
    def square(self):
        self.S_treangle = abs(
            (self.x2 - self.x1) * (self.y3 - self.y1) - (self.x3 - self.x1) * (self.y2 - self.y1)) * 0.5
        return round(self.S_treangle)

    @property
    def height(self):
        print(f"Высота треугольника 1: {round(2 * self.square / self.XY12, 2)}")
        print(f"Высота треугольника 2: {round(2 * self.square / self.XY13, 2)}")
        print(f"Высота треугольника 3: {round(2 * self.square / self.XY23, 2)}")


pointCoordinates = Triangle(0, 0, 10, 0, 5, 0)

print(f"Стороны треугольника: ")
print(f"Сторона 1: {pointCoordinates.XY12}")
print(f"Сторона 2: {pointCoordinates.XY13}")
print(f"Сторона 3: {pointCoordinates.XY23}")
print(f"Периметр треугольника: {pointCoordinates.perimeter}")
print(f"Площадь треугольника: {pointCoordinates.square}")
pointCoordinates.height

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print(f"\nЗадача-2. Написать класс для трапеции, выполнить необходимые вычисления\n")
class Trapezium():
    def __init__(self, x1, x2, x3, x4, y1, y2, y3, y4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.XY12 = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)
        self.XY23 = round(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5, 2)
        self.XY34 = round(((x4 - x3) ** 2 + (y4 - y3) ** 2) ** 0.5, 2)
        self.XY41 = round(((x4 - x1) ** 2 + (y4 - y1) ** 2) ** 0.5, 2)
        self.diagonal13 = round(((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5, 2)
        self.diagonal24 = round(((x2 - x4) ** 2 + (y2 - y4) ** 2) ** 0.5, 2)
        # self.k12 = round((y2 - y1)/ (x2 - x1), 4)
        # self.k23 = round((y3 - y2)/ (x3 - x2), 4)
        # self.k34 = round((y4 - y3) / (x4 - x3), 4)
        # self.k41 = round((y4 - y1) / (x4 - x1), 4)

    @property
    def check_trapezium(self):  # а трапеция ли это?
        if (self.y2 - self.y1) * (self.x4 - self.x3) == (self.x2 - self.x1) * (self.y4 - self.y3) and (self.y3 - self.y2) * (self.x4 - self.x1) == (self.x3 - self.x2) * (self.y4 - self.y1):
            isTrapezium = "AB параллельно CD и BC параллельно DA -> четырехугольник является трапецией и ромбом"
        elif (self.y2 - self.y1) * (self.x4 - self.x3) == (self.x2 - self.x1) * (self.y4 - self.y3):
            isTrapezium = "AB параллельно CD -> четырехугольник является трапецией"
        elif (self.y3 - self.y2) * (self.x4 - self.x1) == (self.x3 - self.x2) * (self.y4 - self.y1):
            isTrapezium = "BC параллельно DA -> четырехугольник является трапецией"
        else:
            isTrapezium = "Четырехугольник не имеет параллельных сторон -> не является трапецией"
        return isTrapezium

    @property
    def check_equilateral(self):
        if self.diagonal13 == self.diagonal24:
            return print("Диагонали равны, трапеция равнобокая")
        else:
            return print("Диагонали НЕ равны, трапеция НЕ равнобокая")

    @property
    def perimeter(self):
        self.perimeterTrapezium = self.XY12 + self.XY23 + self.XY34 + self.XY41
        return round(self.perimeterTrapezium, 2)

    @property
    def square(self):
        self.squareTrapezium = (self.XY23 + self.XY41) / 2 * ((self.XY12**2 - ((self.XY23 - self.XY41)**2 / 4))**0.5)
        return round(self.squareTrapezium)

trap = Trapezium(0, 2, 4, 6, 0, 4, 4, 0)

print(f"{trap.check_trapezium}\n")
trap.check_equilateral
print(f"Стороны фигуры: ")
print(f"Сторона 1: {trap.XY12}")
print(f"Сторона 2: {trap.XY23}")
print(f"Сторона 3: {trap.XY34}")
print(f"Сторона 4: {trap.XY41}")
print(f"Периметр четырехугольника: {trap.perimeter}")
print(f"Площадь четырехугольника: {trap.square}")