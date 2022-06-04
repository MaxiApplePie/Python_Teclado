from collections import deque

friends = deque(('Rolf', 'Bob', 'Anna', 'Jose', 'Lolo'))


def get_friends():
    yield from friends


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'Hello {friend}'
        except StopIteration:
            pass


friends_generator = get_friends()
g = greet(friends_generator)
