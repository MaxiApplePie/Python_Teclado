cars = ['ok', 'ok', 'ok', 'ok', 'ok', 'ok']

for status in cars:
    if status == 'faulty':
        print('Stopping the production line !')
        break
    print(f'The car is {status}')
    print('Shipping new car to the customer')
else:
    print('All the cars were shipped')
