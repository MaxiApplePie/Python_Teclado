art_friends = {"Rolf", "Bob"}
science_friends = {"Harry", "Mike"}
print(art_friends)
art_friends.add("Mike")
print(art_friends)

print(art_friends.intersection(science_friends))
art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

in_both = art_friends.intersection(science_friends)
print(in_both)