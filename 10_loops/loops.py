for x in range(0,11):
    print(x)

x = 0
while x <= 10:
    print(x)
    x += 1
   
x = 11
while x > 0:
    print(x - 1)
    x -= 1
x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] 
for j in x:
    print(j)

n = 1
for i in range(0,7):
    print('#' * n)
    n += 1

for i in range(0,8):
    print('# ' * 8)
    
for i in range(0, 11):
    print(f'{i} x {i} = ' + str(i * i ))
    
lst = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for i in lst:
    print(i)
    
for i in range(0, 101):
    if i % 2 != 0:
        continue
    else:
        print(i)
        
for i in range(0, 101):
    if i % 2 == 0:
        continue
    else:
        print(i)
        
suma = 0        
for i in range(0, 101):
    suma = suma + i
print(suma)

countrie_data =[{
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },]

# Encontrar 
languagis = 0
for dictt in countrie_data:
    for key, value in dictt.items():
        if key == 'languages':
                languagis += 1
print('-------------')
print(languagis)
print('------')
# Encontrar los paises con mayor poblacion
countrie_mayor = 0
for dictt in countrie_data:
    for key, value in dictt.items():
        if key == 'population' and value > 1000000:
            print(value)
            countrie_mayor += 1
print(countrie_mayor)