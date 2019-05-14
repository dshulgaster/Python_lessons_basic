# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

import random

class Person:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
    def get_full_name(self):
        return self.name + " " + self.patronymic + " " + self.surname

class Student(Person):
    def __init__(self, name, patronymic, surname, school, schoolClass):
        Person.__init__(self, name, patronymic, surname)
        self.school = school
        self.schoolClass = schoolClass

class Teacher(Person):
    def __init__(self, name, patronymic, surname, school, schoolClass, subject):
        Person.__init__(self, name, patronymic, surname)
        self.school = school
        self.schoolClass = schoolClass
        self.subject = subject

class Parent(Person):
    def __init__(self):
        pass

class SchoolClass:
    def __init__(self, name):
        self.name = name
        self.students = []
        # self.teachers = []

    @property
    def get_students(self):
        return [itm.full_name for itm in self.students]

class School:
    def __init__(self):
        self.school_classes = []

    @property
    def get_classes(self):
        return [itm.name for itm in self.school_classes]

    @property
    def get_students(self):
        list = []
        for itm in self.school_classes:
            for student in itm.students:
                list.append(student)
        return list

    # def add_student(self, *students):
    #     # for s_cls in self.school_classes:
    #     #     while len(s_cls.students) < 10:
    #     #         student = random.choice(students)
    #     #         if student not in self.get_students:
    #     #             s_cls.students.append(student)
    #     #             student.school_class = s_cls
    #     for i in self.school_classes:   # заполняем студентов для каждого класса
    #         for k in range(10):
    #             # print(students[4])
    #             # student = random.choice(students)
    #             # print(student)

    def __str__(self):
        pass
        # return self.school_classes

class Subject:
    def __init__(self):
        pass

currentSchool = School()

# заполнение данных
namesList = ['Дмитрий', 'Екатерина', 'Владимир', 'Алексей', 'Иван', 'Сергей', 'Ольга', 'Анна', 'Анатолий', 'Мария', 'Максим', 'Петр', 'Кирил', 'Женя', 'Саша', 'Антон']
patronymicsMaleList = ['Николаевич', 'Иванович', 'Сидорович', 'Анатольевич', 'Сергеевич', 'Максимович', 'Петрович', 'Владимирович', 'Евгеньевич', 'Александрович', 'Валерьевич']
patronymicsFemaleList = ['Николаевна', 'Ивановна', 'Сидоровна', 'Анатольевна', 'Сергеевна', 'Максимовна', 'Петрововна', 'Владимировна', 'Евгеньевна', 'Александровна', 'Валерьевна']
surnamesList = ['Иванов', 'Петров', 'Сидоров', 'Кузнецов', 'Рофе', 'Шульга', 'Травин', 'Солодуха', 'Озеров', 'Уткин', 'Майоров']
classesList = ['5а', '5б', '5в', '6а', '6б', '6в','7а', '7б', '7в','9а', '9б', '9в','10а', '10б', '10в']
peoplesList = [Person(name=random.choice(namesList), patronymic=random.choice(patronymicsMaleList),
                      surname=random.choice(surnamesList)) for _ in range(10)]
subjectsList = ['Английский язык', 'Математика', 'Русский язык', 'Физкультура', 'История']
teachersList = [Teacher(name=random.choice(namesList),
                        patronymic=random.choice(patronymicsMaleList), surname=random.choice(surnamesList),
                        school=random.randint(1, 99), schoolClass=random.choice(classesList),
                        subject=random.choice(subjectsList)) for _ in range(15)]
studentsList = [Student(name=random.choice(namesList),
                        patronymic=random.choice(patronymicsMaleList), surname=random.choice(surnamesList),
                        school=random.randint(1, 99), schoolClass=random.choice(classesList)) for _ in range(10)]

currentSchool.school_classes.extend([SchoolClass(itm) for itm in classesList])
# currentSchool.add_student(*studentsList)
print(studentsList)

# 1. Получить полный список всех классов школы
print(currentSchool.get_classes)

# 2. Получить список всех учеников в указанном классе
# print(currentSchool.students)

random_class = random.choice(currentSchool.school_classes)
print(f'В классе {random_class.name}')
print(f'студенты {random_class.get_students}')
# print(f'В классе {random_class.name} учатся: \n{random_class.get_students}')

# 3. Получить список всех предметов указанного ученика
# print(currentSchool.subjects())

# 4. Узнать ФИО родителей указанного ученика
# print(currentSchool.parents())

# 5. Получить список всех Учителей, преподающих в указанном классе
# print(currentSchool.teachers)