def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


print([2*x for x in hundred_numbers()])
