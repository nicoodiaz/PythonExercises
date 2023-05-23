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

#Para acceder al index y al item
for index, item in enumerate([20, 30, 40]):
    print(index, item)


# Descomprimir
countries =  ['Finlandia', 'Suecia', 'Noruega', 'Dinamarca', 'Islandia', 'Estonia', 'Rusia']
*nordic_countries, es, ru = countries
print(nordic_countries, 'es = ' + es, 'ru = ' + ru)


# Packing Lists, a veces no sabemos cuantos argumentos se deben pasar a una funcion
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28