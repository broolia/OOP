class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    

    def average_score(self):
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Студент еще не получал оценки'
        else:
            return f'{middle_sum / len(self.grades.values()):.2f}'
        
  

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    

    def __str__(self):
       res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
       res += f'Средняя оценка за домашние задания:{self.average_score()} \n'
       res += f'Курсы в процессе изучения:{", ".join(self.courses_in_progress)} \n'
       res += f'Завершенные курсы:{self.finished_courses}'
       return res
    

    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'Такого студента нет')
            return
        return self.average_score() < student.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    
    def middle_rate(self):
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Оценки еще не выставлялись'
        else:
            return f'{middle_sum / len(self.grades.values()):.2f}'
        
    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f' Такого лектора нет')
            return
        return self.middle_rate() < lecturer.middle_rate()


     


    def __str__(self):
        return f'Имя : {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_rate()}'


        
        

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя : {self.name} \nФамилия: {self.surname}'
    

student_1 = Student('Марина', 'Петрова', 'Female')
student_1.finished_courses = ['Python', 'C++']
student_1.courses_in_progress = ['Git', 'Java']

student_2 = Student('Карась', 'Карасевич', 'Male')
student_2.finished_courses = ['С++', 'Git']
student_2.courses_in_progress = ['Python', 'Java']
students_list = [student_1, student_2]

lecturer_1 = Lecturer('Александр', 'Хитров')
lecturer_1.courses_attached = ['Git', 'Java']

lecturer_2 = Lecturer('Павел', 'Дуров')
lecturer_2.courses_attached = ['Python']
lecturer_list = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Тамара', 'Гельман')
reviewer_1.courses_attached = ['Python', 'С++', 'Java', 'Git']

reviewer_2 = Reviewer('Евгений', 'Бруев')
reviewer_2.courses_attached = ['Git', 'Python', 'С++']
reviewer_1 = Reviewer('Мила','Сапфирова')
reviewer_2 = Reviewer('Жана','Бруле')

reviewer_1.rate_hw(student_1, 'Git', 4)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_1, 'Java', 10)
reviewer_1.rate_hw(student_1, 'Java', 10)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Python', 6)
reviewer_1.rate_hw(student_1, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_1, 'С++', 10)
reviewer_1.rate_hw(student_1, 'С++', 10)
reviewer_1.rate_hw(student_1, 'С++', 4)

reviewer_2.rate_hw(student_2, 'С++', 4)
reviewer_2.rate_hw(student_2, 'С++', 3)
reviewer_2.rate_hw(student_2, 'С++', 5)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 3)
reviewer_2.rate_hw(student_2, 'Java', 10)

student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Git', 6)
student_1.rate_lecturer(lecturer_1, 'Java', 6)
student_1.rate_lecturer(lecturer_1, 'Java', 4)
student_1.rate_lecturer(lecturer_1, 'Java', 3)

student_2.rate_lecturer(lecturer_1, 'Java', 9)
student_2.rate_lecturer(lecturer_1, 'Java', 7)
student_2.rate_lecturer(lecturer_1, 'Java', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'Python', 2)
student_2.rate_lecturer(lecturer_2, 'Python', 5)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

print(student_1.average_score())
print(student_2.average_score())
print(lecturer_1.middle_rate())
print(lecturer_2.middle_rate())


if student_1 > student_2:
    print(f'{student_1.name} {student_1.surname} учится лучше чем {student_2.name} {student_2.surname}')
else:
    print(f'{student_2.name} {student_2.surname} учится лучше чем {student_1.name} {student_2.surname}')

if lecturer_1 > lecturer_2:
    print(f'{lecturer_1.name} {lecturer_1.surname} преподает лучше чем {lecturer_2.name} {lecturer_2.surname}')
else:
    print(f'{lecturer_2.name} {lecturer_2.surname} преподает лучше чем {lecturer_1.name} {lecturer_1.surname}')



def grades_students(students_list, course):
    overall_student_rating = 0
    lectors = 0
    for student in students_list:
        if course in student.grades.keys():
            average_student_score = 0
            for grades in student.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(student.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{overall_student_rating / lectors:.2f}'


def grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.grades.keys():
            lecturer_average_rates = 0
            for rate in lecturer.grades[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.grades[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{average_rating / b:.2f}'

lecturer_list = [lecturer_1,lecturer_2]
students_list = [student_1, student_2]
print(f'Средняя оценка студентов по курсу "Git": {grades_students(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(students_list, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(lecturer_list, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')