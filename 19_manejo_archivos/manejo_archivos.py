#read(), lee el texto como una cadena
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

#readline(), lee solo la primera linea
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

#readlines(), lee todas las lines y devuelve una lista de estas
f = open('./files/reading_file_example.txt')
lines = f.readlines()
count_line = 0
# for i in lines:
#     count_line += 1
# print(count_line)
# print('Aqui se cuenta las lineas de un txt')
print(type(lines))
print(lines)
f.close()

#Con el metodo 'with', no debemos preocuparnos de cerrar los archivos, los hace por si mismo
with open('./files/reading_file_example.txt') as f:
    #splitlines(), otra forma de obtener todas las lineas
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
