import time
from multiprocessing import Process


def ask_user():
    start = time.time()
    my_user = input('Please, input a user : ')
    print(f'Ask user : {time.time() - start}')


def complex_calculation():
    start = time.time()
    power = [x ** 2 for x in range(20000000)]  # 5.49 seconds
    print(f'complex calc : {time.time() - start}')


if __name__ == '__main__':

    # partie 1
    start = time.time()
    ask_user()
    complex_calculation()
    print(f'-- Single thread ** Temps total: {time.time() - start}.')


    # partie 2
    process = Process(target=complex_calculation)
    process2 = Process(target=complex_calculation)
    process.start()
    process2.start()
    start = time.time()
    process.join()
    process2.join()
    print(f'-- Double thread **  Temps total: {time.time() - start}.')
