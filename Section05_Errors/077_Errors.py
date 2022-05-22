class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError('Input car type !')
        self.cars.append(car)


ford = Garage()
ford.add_car(Car('Ford', 'Focus'))
ford.add_car(Car('Ford', 'Fiesta'))
print(len(ford))