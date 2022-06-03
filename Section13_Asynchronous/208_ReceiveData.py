from collections import deque

friends = deque(('Rolf', 'Bob', 'Anna', 'Jose', 'Lolo'))


def greet():
    friend = yield
    print(f'Hello {friend}.')


g = greet()
g.send(None)  # priming the generator
g.send('Adam')