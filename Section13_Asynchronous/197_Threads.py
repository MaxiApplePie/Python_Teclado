import time
from threading import Thread


def ask_user():
    start = time.time()
    my_user = input('Please, input a user : ')
    print(f'Ask user : {time.time() - start}')


def complex_calculation():
    start = time.time()
    power = [x ** 2 for x in range(20000000)]  # 5.49 seconds
    # print(max(power))
    print(f'complex calc : {time.time() - start}')


# start = time.time()
# print(f'\n-- Debut du traitement')
# ask_user()
# complex_calculation()
# end = time.time()
#
# print(f'-- Temps total: {end - start}.')


thread1 = Thread(target=ask_user)
thread2 = Thread(target=complex_calculation)

start = time.time()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f'-- Temps total: {end - start}.')
