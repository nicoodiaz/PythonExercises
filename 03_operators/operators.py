age = 23
height = 1.72
num_complex = 5j

base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))

area = int(0.5 * base * altura)
print(area)

a = int(input('Ingrese el lado A: '))
b = int(input('Ingrese el lado B: '))
c = int(input('Ingrese el lado C: '))
perimeter = a + b + c
print(perimeter)

largo = int(input('Ingrese el largo del rectangulo: '))
ancho = int(input('Ingrese el ancho del rectangulo: '))

area = largo * ancho
perimeter2 = 2 *(largo + ancho)
print(area, perimeter2)

py = len('Python')
dr = len('dragon')
asd = py == dr
print(not asd)
print('on' in 'python')
print('jerga' in 'Espero que este curso no esté lleno de jerga')