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

    all = letters + nums + simbols
    
    users = []
    
    chars = int(input('Ingrese la cantidad de caracteres: '))
    cant = int(input('Ingrese la cantidad de users: '))
    
    for x in range(cant):
        user_chars = []
        for i in range(chars):
            caracter_random = random.choice(all)
            user_chars.append(caracter_random)
        users_id = ''.join(user_chars)
        users.append(users_id)
    return users

print(user_id_gen_by_user())