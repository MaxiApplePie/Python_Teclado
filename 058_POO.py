my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 80, 88, 95]
}


def calc_average(student):
    avg = sum(student['grades']) / len(student['grades'])
    return avg


print(calc_average(my_student))
