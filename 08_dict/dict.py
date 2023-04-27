dog = {
    'name': '',
    'color': '',
    'breed': '',
    'legs': '',
    'age': 23
}

student = {
    'first_name': '',
    'last_name': '',
    'gender': '',
    'age': 23,
    'material_status': '',
    'skills': ['Python', 'SQL', 'Django', 'FastAPI', 'HTML'],
    'country': '',
    'city': '',
    'address': '',
}

print(len(dog))
print(type(student['skills']))
# El método get devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.
print(student.get('baba'))
# Para agregar a una lista dentro de un diccionario
student['skills'].append('Flask')
print(student['skills'])
#Para obtener las keys del dict como una lista
keys = student.keys()
print(keys)
#Para obtener los values del dict como una lista
value = student.values()
print(value)
#Cambiar el dict a una lista de tuplas
lst = student.items()
print(lst)
#Eliminar un elemento .pop('key') / .popitem() elimina ultimo key / del dict['key]
print(student.popitem())

del student
#print(student) Da error, ya que se lo elimino