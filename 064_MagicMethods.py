class Student:
    def __init__(self, name):
        # print(self)
        self.name = name
        # print(self.name)


s = Student('Bob')


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, idx):
        return self.cars[idx]

    def __repr__(self):
        return f'<Garage {self.cars}>'


ford = Garage()
print(ford)
ford.cars.append('Fiesta')
ford.cars.append('Focus')
print(ford.cars)

# print(len(ford))
# print(ford[0])

for car in ford.cars:
    print(car)