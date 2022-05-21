import json

file = open('friends_json.txt', 'r')
content = json.load(file)

file.close()
print(content['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Focus'},
    {'make': 'Ford', 'model': 'Fiesta'}
]


file1 = open('cars_json.txt', 'w')
json.dump(cars, file1, indent=4)
file1.close()
