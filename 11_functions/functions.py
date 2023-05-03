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

def reverse_list(mtr):
    for i in mtr:
        print(i[-1])
print(reverse_list([1, 2, 3, 4, 5]))