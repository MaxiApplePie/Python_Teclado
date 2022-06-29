"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""


def prime_generator(bound):
    # your code starts here (delete the pass):
    for n in range(2, bound):
        # Prime number
        for j in range(2, n):
            if n % j == 0:
                break
        else:
            yield n


g = prime_generator(17)
print(g)
print(g)
print(g)
print(g)
print(g)
