nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friend = input('Input a name >> ')
# Add the name to the empty set
user_friends.add(friend)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
in_both = nearby_people.intersection(user_friends)
print(in_both)