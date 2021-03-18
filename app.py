weight = input('Weight: ')
measurement = input('(L)bs or (k)g: ')

if measurement.upper() == 'L':
    print(f'you weigh {weight} pounds')
else:
    print(f'you wiegh {weight} kilograms')

# / will return a float, // will retrun a int