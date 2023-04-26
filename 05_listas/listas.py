lst = list()

lst = ['Nico', 'Diaz', 23, 'Rojo', 'Pizza']

print(len(lst))

print(lst[0])
print(lst[2])
print(lst[4])

tipos_de_datos_mixtos = ['Nicolas', 'Diaz', 1.72, 'Soltero', 'Arg-Tuc']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))

print(it_companies[0])
print(it_companies[1])
print(it_companies[-1])

it_companies[1] = 'Mozilla'
print(it_companies)

it_companies.append('Google')
print(it_companies)

it_companies.insert(4, 'Platzi')
print(it_companies)

it_companies[4] = 'PLATZI'
print(it_companies)

exist = 'Mercado Libre' in it_companies
print(exist)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

print(it_companies[0:3])
print(it_companies[6:])

it_companies.pop(0)
print(it_companies)

it_companies.pop(3)
it_companies.pop(3)
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(ages[4])
age_prom = sum(ages) / 10
print(age_prom)
age_range = ages[-1] - ages[0]
print(age_range)