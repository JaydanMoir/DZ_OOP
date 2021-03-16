class Student:
    all_students = {}
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #законченные курсы
        self.courses_in_progress = [] #текущие курсы, которые сейчас изучаются
        self.grades_students = {} #оценки
        self.full_name = self.name + " " + self.surname

    #завершенные курсы студента
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # выставление оценок лектору
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    #добавение всех студентов с оценками в словарь
    def add_student(self):
        Student.all_students[self.full_name] = self.grades_students
        return Student.all_students

    #средня оценка студента за ДЗ
    def avarage_grade_st(self):
        self.lst_grades_st = []
        self.all_grades_st = []

        for self.lst_grades_st in self.grades_students.values():
            for grade in self.lst_grades_st:
                self.all_grades_st.append(grade)
        try:
            avarage_grade = round(sum(self.all_grades_st) / len(self.all_grades_st), 1)
        except ZeroDivisionError:
            avarage_grade=0
        return avarage_grade

    #средняя оценка всех студентов на курсе
    @classmethod
    def avarage_grade_all_st(cls, all_students, course):
        all_grade_st = [] #список всех оценок на текущем курсе
        for grade_course in all_students.values():
            for some_course, val in grade_course.items():
                if some_course == course:
                    for gr in val:
                        all_grade_st.append(gr)
        
        return (f"Средняя оценка студентов по курсу {course}: {round((sum(all_grade_st)/len(all_grade_st)), 1)}")

    #переопределение метода
    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avarage_grade_st()} \n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress) } \nЗавершенные курсы: {', '.join(self.finished_courses)}\n__________________")

    # переопределение метода
    def __gt__(self, other_st):
        if not isinstance(other_st, Student):
            return "Нет такого студента"
        if self.avarage_grade_st() > other_st.avarage_grade_st():
            return (f"Лучший студент по средней оценке: {self.name} {self.surname}")
        else:
            return (f"Лучший студент по средней оценке: {other_st.name} {other_st.surname}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #закрепленные курcы за преподавателем

#Лекторы
class Lecturer(Mentor):
    all_lecturers = {}

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {} #оценки лекторов
        self.full_name = self.name + " " + surname

    #добавение всех лекторов с оценками в словарь
    def add_lec(self):
        Lecturer.all_lecturers[self.full_name] = self.grades_lecturer
        return Lecturer.all_lecturers

    #средняя оценка за лекцию
    def avarage_grade_lec(self):
        self.lst_grades_lec = [] #список оценок за определенную лекцию
        self.all_grades_lect = []

        for lst_grades_lec in self.grades_lecturer.values():
            for grade in lst_grades_lec:
                self.all_grades_lect.append(grade)

        try:
            avarage_grade = round(sum(self.all_grades_lect) / len(self.all_grades_lect), 1)
        except ZeroDivisionError:
            avarage_grade=0
        return avarage_grade

    # средняя оценка всех лекторов на курсе
    @classmethod
    def avarage_grade_all_lec(cls, all_lecturers, course):
        all_grade_lec = []
        for grade_course in all_lecturers.values():
            for some_course, val in grade_course.items():
                if some_course == course:
                    for gr in val:
                        all_grade_lec.append(gr)

        return (f"Средняя оценка лекторов по курсу {course}: {round((sum(all_grade_lec) / len(all_grade_lec)), 1)}")

    # переопределение метода
    def __gt__(self, other_lect):
        if not isinstance(other_lect, Lecturer):
            return "Нет такого лектора"
        if self.avarage_grade_lec() > other_lect.avarage_grade_lec():
            return (f"Лучший преподаватель по средней оценке: {self.name} {self.surname}")
        else:
            return (f"Лучший преподаватель по средней оценке: {other_lect.name} {other_lect.surname}")

    # переопределение метода
    def __str__(self):
       return (f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avarage_grade_lec()}\n__________________")


#эксперты, проверяющие домашние задания
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_st(self, student, course, grade): # выставление оценок
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_students:
                student.grades_students[course] += [grade]
            else:
                student.grades_students[course] = [grade]
        else:
            return 'Ошибка'

    # переопределение метода
    def __str__(self):
        return (f"Имя: {self.name} \nФамилия: {self.surname}\n__________________")


#создание обЪектов класса Student
student1 = Student('Alex', 'Len', 'man')
student1.courses_in_progress += ['Java']
student1.courses_in_progress += ["Git"]
student1.courses_in_progress += ["C++"]
student1.courses_in_progress += ["Python"]
student1.add_courses("Английский язык")
student1.add_student()

student2 = Student("Kate", "Entony", "woman")
student2.courses_in_progress += ["Java"]
student2.courses_in_progress += ["C++"]
student2.courses_in_progress += ["Python"]
student2.add_student()

student3 = Student("Jesika", "Noris", "woman")
student3.courses_in_progress += ["Python"]
student3.add_student()

#создание обЪектов класса Reviewer
reviewer1 = Reviewer('David', 'Jons')
reviewer1.courses_attached += ['Java']
reviewer1.rate_st(student1, "Java", 6)

reviewer2 = Reviewer("Jon", "James")
reviewer2.courses_attached += ["Git"]
reviewer2.rate_st(student1, "Git", 8)

reviewer3 = Reviewer("Bella", "Noris")
reviewer3.courses_attached += ["Python"]
reviewer3.rate_st(student1,"Python",7)
reviewer3.rate_st(student2, "Python", 9)
reviewer3.rate_st(student3, "Python", 10)

#создание обЪектов класса Lecturer
lecturer1 = Lecturer("Max", "Brock")
lecturer1.courses_attached += ["Java"]
lecturer1.courses_attached += ["Python"]
lecturer1.add_lec()

lecturer2 = Lecturer("Tomas", "Anderson")
lecturer2.courses_attached += ["C++"]
lecturer2.add_lec()

student1.rate_lect(lecturer1, "Java", 7)
student2.rate_lect(lecturer1, "Java", 9)
student3.rate_lect(lecturer1, "Python", 10)

student1.rate_lect(lecturer2, "C++", 10)
student2.rate_lect(lecturer2, "C++", 8)


reviewer1.rate_st(student1, 'Python', 10)
reviewer2.rate_st(student1, "Git", 8)
reviewer1.rate_st(student2, "Java",9)


print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)
print(lecturer1 > lecturer2)
print(student1 > student2)

print("_____________")
print(Student.avarage_grade_all_st(Student.all_students, "Python"))
print(Lecturer.avarage_grade_all_lec(Lecturer.all_lecturers, "C++"))



