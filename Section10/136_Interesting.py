from collections import Counter, defaultdict, OrderedDict, namedtuple, deque


# Counter
device_temp = [3.5, 14.0, 14.0, 14.5, 14.8, 16.0]

temp_counter = Counter(device_temp)
print(temp_counter[14.0])
print(type(temp_counter))

print(Counter({'hello': 5, 'hi': 3})['hi'])

# deque
print('** deque ********************************************************')

friends = deque(('Rolf', 'Jen', 'Anna'))
friends.append('Lolo')
print(friends)
friends.appendleft('Bob')


# namedtuple
print('** namedtuple ********************************************************')

account = ('checking', 568.23)
print(account[0])  # name
print(account[1])  # balance

Account = namedtuple('Account', ['name', 'balance'])
account = Account('checking', 568.23)
print(account.name)
print(account)


# ordereddict
print('** ordereddict ********************************************************')
o = OrderedDict()
o['Rolf'] = 6
o['Jose'] = 12
o['Lolo'] = 31
print(o)
o.move_to_end('Rolf')
print(o)
o.move_to_end('Lolo', last=False)
print(o)
o.popitem()

# defaultdict
print('** defaultdict ********************************************************')
# my_dict = {'hello': 4}
# print(my_dict['hi'])

coworkers = [('Rolf', 'MIT'), ('Anna', 'Oxford'), ('Rolf', 'Cambridge')]
alma_maters = defaultdict(list)

for coworker, place in coworkers:
    # alma_maters.append({coworker[0]: coworker[1]})
    alma_maters[coworker].append(place)

print(alma_maters)
print(alma_maters['Rolf'])
print(alma_maters['Bob'])