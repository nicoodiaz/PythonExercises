import random
import string



def random_user_id():
    letters = string.ascii_letters
    nums = string.digits
    simbols = string.punctuation

    all = letters + nums + simbols
    user = []
    for i in range(0, 6):
        caracter_random = random.choice(all)
        user.append(caracter_random)
    user = ''.join(user)
    return user
print(random_user_id())

print('--------------')

def user_id_gen_by_user():
    letters = string.ascii_letters
    nums = string.digits
    simbols = string.punctuation

    all_chars = letters + nums + simbols
    
    users = []
    
    chars = int(input('Ingrese la cantidad de caracteres: '))
    cant = int(input('Ingrese la cantidad de users: '))
    
    for x in range(cant):
        user_chars = []
        for i in range(chars):
            caracter_random = random.choice(all_chars)
            user_chars.append(caracter_random)
        users_id = ''.join(user_chars)
        users.append(users_id)
    return users

print(user_id_gen_by_user())


def rgb_color_gen():
    nums = range(255)
    n = 0
    rgb = []
    while n != 3:
        ale = random.choice(nums)
        rgb.append(ale)
        n += 1
    return rgb

print(rgb_color_gen())

print('---------Exercise lvl2-------------')

def list_of_hexa_colors(cant):
    colors = []
    for i in range(cant):
        color_hex = '#' + ''.join([random.choice('0123456789abcdef') for j in range(6)])
        colors.append(color_hex)
    return colors

print(list_of_hexa_colors(5))