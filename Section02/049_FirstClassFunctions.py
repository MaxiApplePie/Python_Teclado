def greet():
    print('Hello !')


hello = greet

hello()

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

students = [
    {'name': 'Rolf', 'grades': (1, 3, 5, 7, 9, 11)},
    {'name': 'Charlie', 'grades': (2, 7, 9, 22, 10, 5)},
    {'name': 'Anna', 'grades': (13, 14, 15, 16, 17, 18)},
    {'name': 'Jen', 'grades': (19, 20, 12, 7, 3, 5)}
]

for student in students:
    print(avg(student['grades']))


to_uppercase = lambda text: text.upper()
print(to_uppercase('bob'))