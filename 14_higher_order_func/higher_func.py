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