def suma_dos_numeros(x,y):
    return x + y

print(suma_dos_numeros(3,5))

def area_of_circle(r):
    area = 3.14 * r**2
    return area
print(area_of_circle(4))

def add_all_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print(add_all_nums(2,3,5))

def convert_celsius_to_fahrenheit(C):
    fahrenheit = (C*9/5) +32 
    return fahrenheit
print(convert_celsius_to_fahrenheit(14))

def check_temporate():
    mes = input('Plase input a mounth of the year: ')
    if mes in ('December', 'January', 'February'):
        print('You are in Summer')
    elif mes in ('March', 'April', 'May'):
        print('You are in Autumn')
    elif mes in ('June', 'July', 'August'):
        print('You are in Winter')
    elif mes in ('September', 'October', 'November'):
        print('You are in Spring')
    else:
        print('Please, input a correct mounth')
    
check_temporate()

# def solve_quadratic_eqn(x, a , b, c):
#     salve = a*x ** + b*x + c
#     return salve
# print(solve_quadratic_eqn(4,3,4,3))

def print_lst(lst):
    for i in lst:
        print(i)
print_lst([1,4,6,4,2,11,456,1234,123, 'asd', 'basd'])

def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1): #El len(lst)-1, para encontrar el ultimo indice
                                        #El -1 para indicar que el bucle se detenga en i = -1
                                        #El ultimo para decrementar el valor de i en cada iteracion        
        reversed_lst.append(lst[i])
    return reversed_lst
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

def capitalize_list_items(lst):
    new_lst = []
    for i in lst:
        new_lst.append([i.upper()])
    return new_lst
print(capitalize_list_items(['asd', 'dsa', 'bsa', 'gfd']))

# def add_item(lst, item):
#     new_lst = []
#     lst2 = list(lst)
#     lst2.append(item)
#     new_lst.append(lst2)
#     return new_lst
def add_item(lst, item):
    lst.append(item)
    return lst
food = ['Melon', 'Ciruela', 'Frutilla', 'Banana']
print(add_item(food, 'Mango'))

food = ['Melon', 'Ciruela', 'Frutilla', 'Banana', 'Kiwi']
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(food, 'Kiwi'))

def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total
print(sum_of_odds(6))
print(sum_of_odds(9))

def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total
print(sum_of_odds(6))
print(sum_of_odds(9))

def evens_and_odds(n):
    odds = 0
    evens = 0
    for i in range(n + 1):
        if i % 2 != 0:
            odds += 1
        else:
            evens += 1
    return odds, evens
print(evens_and_odds(100))
            
            
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(15))