class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def avr(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            averg = sum(all_grades) / len(all_grades)
        else:
            averg = 0
        return averg
    
    def __ge__(self, lector):
        if isinstance(lector, Lecturer):
            return self.avr() >= lector.avr()
        
    
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avr()}\n'
        f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avr()}'
    
    def avr(self):
        all_grades = [score for scores in self.grades.values() for score in scores]
        if all_grades:
            averg = sum(all_grades) / len(all_grades)
        else:
            averg = 0
        return averg


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    
def avr_grade_students(students, course):
    sum_grades = 0
    count_grades = 0
    for student in students:
        if course in student.grades:
            for grade in list(student.grades[course]):
                sum_grades += grade
                count_grades += 1
    grade_avr = sum_grades / count_grades
    return grade_avr

def avr_grade_lecturer(lecturer, course):
    sum_grades = 0
    count_grades = 0
    for lecture in lecturer:
        if course in lecture.grades:
            for grade in list(lecture.grades[course]):
                sum_grades += grade
                count_grades += 1
    grade_avr = sum_grades / count_grades
    return grade_avr



    
student = Student('Sergey', 'Sergeev', 'male')
student.courses_in_progress += ['Python']
student.finished_courses += ['Системный администратор Linux']
student.courses_in_progress += ['Java']

student1 = Student('Sveta', 'Svetikova', 'female')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Java']
student1.courses_in_progress += ['Java']

lector = Lecturer('Petr', 'Petrov')
lector.courses_attached += ['Python']

lector1 = Lecturer('Maxim', 'Maximov')
lector1.courses_attached += ['Python']

rew = Reviewer('Ivan', 'Ivanov')
rew.courses_attached += ['Python']

rew1 = Reviewer('Angelina', 'Joly')
rew1.courses_attached += ['Java']

student1.rate_hw(lector1, 'Java', 6)
student.rate_hw(lector, 'Python', 8)
student.rate_hw(lector1, 'Java', 10)


rew1.rate_hw(student1, 'Java', 10)
rew.rate_hw(student, 'Python', 7)
rew1.rate_hw(student,'Java', 9)

if student.avr() >= lector.avr():
    print(f"Средняя оценка у {student.name} больше чем у {lector.name}")
else:
    print(f"Средняя оценка у {student.name} больше чем у {lector.name}")

print()
print(rew)
print()
print(lector)
print()
print(student)
print()
print(rew1)
print()
print(lector1)
print()
print(student1)
print()
print('Средняя оценка лекторов на курсе Python = ' + str(avr_grade_lecturer([lector, lector1], 'Python')))
print('Средняя оценка студентов на курсе Python = ' + str(avr_grade_students([student, student1], 'Python')))