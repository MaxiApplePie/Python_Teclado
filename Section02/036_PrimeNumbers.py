
for n in range (2, 100):
    # Prime number
    for j in range(2, n):
        if n % j == 0:
            break
    else:
        print(f'{n} is a prime number !')