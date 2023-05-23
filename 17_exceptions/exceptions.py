# try:
#     Ejecuta este codigo si todo va bien
# except:
#     Si algo sale mal, ejecuta este codigo

try:
    print(10 + '5')
except:
    print('Algo salio mal')

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2023 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)