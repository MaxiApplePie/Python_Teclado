my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 80, 88, 95]
}


def calc_average(student):
    avg = sum(student['grades']) / len(student['grades'])
    return avg


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student_1 = Student('Rolf Smith', [70, 80, 88, 95])
student_2 = Student('Rolf Smith', [50, 77, 88, 91])
print(student_1.__class__)

print(student_1.average())
print(Student.average(student_1))
print(student_2.average())


def average(student):
    return sum(student.grades) / len(student.grades)


print(average(student_1))


