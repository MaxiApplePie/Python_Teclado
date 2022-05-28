friends = {
    'Rolf': 31,
    'Lolo': 51,
    'Vera': 42
}

print(friends)

another_friends = friends

print(id(friends))
print(id(another_friends))

friends['Daniil'] = 1
print(friends)
print(another_friends)

