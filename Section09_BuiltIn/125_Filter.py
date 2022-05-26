# def start_with_a(friend):
#     return friend.startswith('A')
#

friends = ['Anna', 'Bob', 'Amy', 'Rolf']
start_with_a = filter(lambda friend: friend.startswith('A'), friends)

print(next(start_with_a))
print(next(start_with_a))

geb = (x for x in friends if x.startswith('A'))
print(type(geb))
print(type(start_with_a))