age = int(input('Enter your age: '))

if age >= 18:
    print('You are old enough to learn to drive')
else:
    more_age = 18 - age
    print(f'You need {more_age} more years to learn to drive')
    
my_age = 23
your_age = int(input('Enter your age: '))



if my_age > your_age:
    if my_age - your_age == 1:
        print('Solo te llevo 1 año')
    elif my_age - your_age > 1:
        diff = my_age - your_age
        print(f'Soy mayor por {diff} años')
elif my_age < your_age:
    diff = your_age - my_age
    print(f'Tu eres mayor por {diff} años')
else:
    print('Ambos tenemos la misma edad ')


num_1 = int(input('Ingresa un numero: '))
num_2 = int(input('Ingresa otro numero: '))

if num_1 > num_2:
    print(f'{num_1} es mayor que {num_2}')
elif num_1 < num_2:
    print(f'{num_2} es mayor que {num_1}')
else:
    print(f'{num_1} es igual que {num_2}')
    

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input('Ingrese una fruta: ')

if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('Esa fruta ya existe en la lista') 