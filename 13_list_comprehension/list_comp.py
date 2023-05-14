numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

neg_and_cero = [i for i in numbers if i <= 0]
print(neg_and_cero)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_lst = [number for row in list_of_lists for x in row for number in x]
print(one_lst)

list_tuple = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_tuple)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

count_2 = [[country.upper(), country[0:3].upper(), capital.upper()] for [[country, capital]] in countries]
print(count_2)

print('-------')

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
count_3 = [{'country': country.upper(), 'city': city.upper()} for [[country, city]] in countries]
print(count_3)

print('-------')
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

string = [f'{name} {lastname}' for [[name, lastname]] in names]
print(string)

print('-------')

