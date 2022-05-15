range_set = {i for i in range(5,15)}
print(range_set)

friends = ['Rolf', 'Jen', 'Anna', 'Eric']
time_since_seen = [5, 4, 7, 5]
long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 4
}

print(long_timers)