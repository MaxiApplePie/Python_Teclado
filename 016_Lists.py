friends = ['Rolf', 'Jeff', 'Anne']
print(friends[1])

friends2 = [
    ['Rolf', 24],
    ['Jeff', 55],
    ['Anne', 41]
]

print(friends2[1])
friends2.append(['Bob', 14])
print(len(friends2))
friends2.remove(['Jeff', 55])
print(len(friends2))
print(friends2)
friends2.pop()
print(friends2)
