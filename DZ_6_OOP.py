#1. Класс - Студент**********************************
class Student:

    list_stud_all = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['С++', 'C#']
        self.courses_in_progress = []
        self.grades = {}
        #добавляем в список имена всех экземпляров студентов
        self.list_stud_all.append(self.name)


    #1.1_Метод оценки лектора, через Студента
    def grade_lect(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grade_lect:
                lector.grade_lect[course] += [grade]
            else:
                lector.grade_lect[course] = [grade]

        else:
            print('Лектор не относится к нашему ВУЗу')

    #1.2_Метод str для студента

    #1.2.1_Метод расчета средней оценки Студента
    def sr_grade(self, course):
        sum_g = sum(self.grades[course])
        lenght_g = len(self.grades[course])
        res = sum_g / lenght_g
        return res

    #1.2.2_Метод перевода списка в строку 1
    def str_list(self):
        res = ','.join(self.courses_in_progress)
        return res

    #1.2.3_Метод перевода списка в строку 2
    def str_list2(self):
        res = ','.join(self.finished_courses)
        return res

    #1.2.4_Метод STR
    def __str__(self):
        res = print (f"\nДанные студента:\nИмя:  {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.sr_grade('Python1')}\nКурсы, в процессе изучения: {self.str_list()}\nКурсы завершенные: {self.str_list2()}")
        return res

    # 1.2.5_Магическтй метод сравнения оценок Лекторов
    def __lt__(self, other):
        return self.sr_grade('Python1') < other.sr_grade('Python1')

#2. Класс - Ментор**********************************
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


#3. Класс - Лектор**********************************
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_lect = {}

    #3.1_Метод расчета средней оценки Лектора
    def sr_grade(self, course):
        sum_g = sum(self.grade_lect[course])
        lenght_g = len(self.grade_lect[course])
        res = sum_g / lenght_g
        return res


    # 3.3_Магическтй метод сравнения оценок Лекторов
    def __lt__(self, other):
        return self.sr_grade('Python1') < other.sr_grade('Python1')


    #3.2_Метод str для Лектора
    def __str__(self):
        res = print (f"\nДанные лектора:\nИмя:  {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.sr_grade('Python1')}")
        return res



#4. Класс - Ревьюер**********************************
class Reviewer (Mentor):

    #4.1_Метод оценки студента силами Ревьюера
    def rate_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]

            else:
                student.grades[course] = [grade]
        else:
            print('Залетный студент. Не относится к нашему ВУЗу')

    #4.2_Метод __str__ для Ревьюера
    def __str__(self):
        res = print (f'Данные ревьюера:\nИмя:  {self.name}\nФамилия: {self.surname}\n')
        return res


# СОЗДАЕМ ЭКЗЕМПЛЯРЫ ********************************************************
#1. Студенты
student1 = Student('Антон', 'Уранов', 'Муж.')
student1.courses_in_progress.append('Python1')
student1.courses_in_progress.append('Python2')
student1.courses_in_progress.append('Java')


student2 = Student('Иван', 'Иванов', 'Муж.')
student2.courses_in_progress.append('Python1')
student2.courses_in_progress.append('Python2')




#2. Лекторы
lector1 = Lecturer('Владимир', 'Лекторов')
lector2 = Lecturer('Лектор', 'Владимиров')

lector1.courses_attached.append('Python1')
lector2.courses_attached.append('Python1')

#3. Ревьюеры
rev1 = Reviewer('Ревьюер', 'Иванов')
rev1.courses_attached.append('Python1')
rev1.courses_attached.append('Python2')


rev2 = Reviewer('Иван', 'Ревьюеров')


# ПОДКЛЮЧАЕМ МЕТОДЫ *********************************************************

#1. Ревьюер ставит оценку студентам
rev1.rate_grade(student1, 'Python1', 5)
rev1.rate_grade(student1, 'Python1', 9)

rev1.rate_grade(student1, 'Python2', 3)
rev1.rate_grade(student1, 'Python2', 5)

rev1.rate_grade(student2, 'Python1', 5)
rev1.rate_grade(student2, 'Python1', 5)

rev1.rate_grade(student2, 'Python2', 10)
rev1.rate_grade(student2, 'Python2', 8)

#2. Студент ставит оценку Лекторам
student1.grade_lect(lector1, 'Python1', 5)
student1.grade_lect(lector1, 'Python1', 4)
student1.grade_lect(lector1, 'Python1', 3)

student1.grade_lect(lector2, 'Python1', 7)
student1.grade_lect(lector2, 'Python1', 8)



# ВЫВОДИМ РЕЗУЛЬТАТЫ*********************************************************
print("\n1. Выводим данные Cтудентов, Ревьюеров и Лекторов:\n")
rev1.__str__()
rev2.__str__()

print("__________________")

lector1.__str__()
lector2.__str__()

print("__________________")

student1.__str__()
student2.__str__()

print("__________________")


# Выводим сравнение Лекторов и Студентов по оценкам
print("\n2. Сравниваем средние оценки лекторов и студентов:\n")
if (lector1 < lector2):
    print(f'Средняя оценка лектора по имени {lector1.name} < оценки лектора по имени {lector2.name}')
else:
    print(f'Средняя оценка лектора по имени {lector1.name} > оценки лектора по имени {lector2.name}')



if (student1 < student2):
    print(f'Средняя оценка студента по имени {student1.name} < оценки лектора по имени {student2.name}')
else:
    print(f'Средняя оценка студента по имени {student1.name} > оценки лектора по имени {student2.name}')

print("__________________")



#Итоговые функции
print("\n3. Выводим средние оценки Студентам и Лекторам:\n")

# 1_Функция - Средняя оценка студентов


list_stud = [student1, student2]

def f_sred_stud (list_stud, course):
    i = 0
    r_g = 0
    count = 0
    for res in list_stud:
        ocenka = list_stud[i].grades[course]
        sum_grade = sum(ocenka)
        lenght_list = len(ocenka)
        result = sum_grade / lenght_list

        # для проверки оценок:
        print(f'Cредняя оценка Студента по имени {list_stud[i].name} : {result}')

        r_g += result
        count += 1
        i += 1


    itog = r_g / count
    print(f'Средняя оценка за домашние задания по всем Cтудентам в рамках курса: {course} составляет: {itog}\n')

# 2_Функция средняя оценка Лекторов

list_lec = [lector1, lector2]

def f_sred_lect (list_lec, course):
    i = 0
    r_g = 0
    count = 0
    for res in list_lec:
        ocenka = list_lec[i].grade_lect[course]
        sum_grade = sum(ocenka)
        lenght_list = len(ocenka)
        result = sum_grade / lenght_list

        # для проверки оценок:
        print(f'Cредняя оценка Лектора по имени {list_lec[i].name} : {result}')

        r_g += result
        count += 1
        i += 1


    itog = r_g / count
    print(f'Средняя оценка всем Лекторам в рамках курса: {course} составляет: {itog}\n')


#Запуск функций





f_sred_stud(list_stud, 'Python1')
f_sred_lect(list_lec, 'Python1')











































