def coutdown(n):
    while n > 0:
        yield n
        n -= 1


tasks = {coutdown(10), coutdown(5), coutdown(20)}
while tasks:
    task = tasks.pop()
    try:
        x = next((task))
        print(x)
        tasks.add(task)
    except StopIteration:
        print('Job is over...')
