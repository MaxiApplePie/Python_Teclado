numbers = [0, 1, 2, 3, 4, 5, 6]
doubled_numbers = [2 * n for n in numbers]

print(doubled_numbers)

friends_ages = [22, 33, 38, 25]
age_strings = [f'Your age is {age}' for age in friends_ages]
print(age_strings)

odds = [age for age in friends_ages if age % 2 ==0]
print(odds)