friend_ages = {"Rolf":41, "Adam":24, "Jane":58}
print(friend_ages["Rolf"])

friend = (
    {"name": "Bob Smith", "age": 45},
    {"name": "Smith", "age": 33},
    {"name": "Jane", "age": 15},
)

print(friend[0])
print(friend[0]["name"])
print(type(friend))
friend_list = list(friend)
print(type(friend_list))
print(friend)
print(friend_list)
print(len(friend_list))


