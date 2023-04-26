my_tuple = tuple()
my_tuple2 = ()

brothers = ('Joaquin', 'Maximiliano')
sisters = ('Micaela', 'Camila')

siblings = brothers + sisters

print(len(siblings))

siblings_2 = list(siblings)
siblings_2.append('Roberto')
siblings_2.append('Silvina')
print(siblings_2)

family_members = tuple(siblings_2)

siblings = family_members[0:4]
print(siblings)

fruits = ('Banana', 'Apple', 'Orange', 'Mango')
vegetables = ('Potato', 'Carrot', 'Tomato', 'Onion')
animal_product = ('Beef', 'Cheese', 'Milk')

food_stuff_tp = fruits + vegetables + animal_product

food_stuff_lp = list(food_stuff_tp)
print(food_stuff_lp)
print(food_stuff_lp[5:6])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)