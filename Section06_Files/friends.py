# Ask friends
friends_three = input('Enter three friends : ')
friends = friends_three.split()
print(friends)

# Check friends in people nearby
people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
print(people_nearby)
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')
for friend in friends_nearby_set:
    print(f'Friend {friend} is near by !')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()

