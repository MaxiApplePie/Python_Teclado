cars = [
    {'make': 'Ford', 'model': 'Fiesta', 'mileage': 23000, 'fuel_consumed': 460},
    {'make': 'Ford', 'model': 'Focus', 'mileage': 17000, 'fuel_consumed': 350},
    {'make': 'Mazda', 'model': 'MX-5', 'mileage': 93000, 'fuel_consumed': 900},
]


def calculate_mpg(car_to_calculate):
    mpg = round(car_to_calculate['mileage'] / car_to_calculate['fuel_consumed'], 2)
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


for car in cars:
    mpg = calculate_mpg(car)
    name = car_name(car)
    print(f"{name} does {mpg} miles per gallon.")
