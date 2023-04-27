it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Mozilla', 'Mercado Libre', 'Meta', 'Tesla'])
print(it_companies)

compani_remove = it_companies.pop()
print(it_companies)
print(compani_remove)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)

# La intersección devuelve un conjunto de elementos que están en ambos conjuntos
print(A.intersection(B))

print(A.issubset(B))

#Si dos conjuntos no tienen un elemento o elementos comunes, los llamamos conjuntos disjuntos
print(A.isdisjoint(B))

# Devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos
print(A.symmetric_difference(B))

del A
del B
del C
print('-----------------------------------------------')

age = [22, 19, 24, 25, 26, 24, 25, 24]

st_age = set(age)
print(st_age)
print(len(age) > len(st_age))

frase = 'Soy profesora y me encanta inspirar y enseñar a la gente'
frase2 = frase.split()
print(frase2)
frase_st = set(frase2)
print(frase_st)
print(len(frase_st))