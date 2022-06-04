def coutdown(n):
    while n > 0:
        yield n
        n -= 1


c2 = coutdown(10)
c1 = coutdown(20)
print(next(c2))
print(next(c1))

print(next(c2))
print(next(c1))
