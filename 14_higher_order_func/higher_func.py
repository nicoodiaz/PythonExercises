from functools import reduce


#Funcion como parametro
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15


#Funcion como valor return
def square(x):          
    return x ** 2

def cube(x):            
    return x ** 3

def absolute(x):        
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): 
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Hola como estas'
print(greeting())   # WELCOME TO PYTHON

@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())

def sum_decorator(function):
    def suma():
        func = function()
        suma_func = sum(func)
        return suma_func
    return suma


@sum_decorator
def lst_sm():
    return [1,2,3,4]
print(lst_sm())

print('---------')

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

print('---Ejercicios---')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

countries_upper = list(map(lambda x: x.upper(), countries))
print(countries_upper)

print('---')

square_lst = list(map(lambda x: x ** 2, numbers))
print(square_lst)

print('---')

names_upper = list(map(lambda x: x.upper(), names))
print(names_upper)

print('---')

is_landin = list(filter(lambda x: 'land' in x, countries))
print(is_landin)

print('---')

six_char = list(filter(lambda x: len(x) == 6, countries))
print(six_char)

print('---')

moresix_char = list(filter(lambda x: len(x) > 6, countries))
print(moresix_char)

print('---')

start_with_e = list(filter(lambda x: x.startswith('E'), countries))
print(start_with_e)

print('---')

my_list = [10, "Hello", True, "Python", 3.14, "World"]
lst_str = list(filter(lambda x: isinstance(x, str), my_list))
print(lst_str)

# sum_red = list(reduce(lambda x, y: x + y, numbers))
# print(sum_red)