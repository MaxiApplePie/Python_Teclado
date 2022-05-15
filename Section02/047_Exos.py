def add(x, y=3):
    total = x + y
    return total


print(add(y=5))


def over_age(data, getter):
    return getter(data) >= 18


user = {'username': 'rolf123', 'age': '35'}

print(over_age(user, lambda x: int(x['age'])))