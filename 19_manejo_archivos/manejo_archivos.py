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
print(type(lines))
print(lines)
f.close()

#Con el metodo 'with', no debemos preocuparnos de cerrar los archivos, los hace por si mismo
with open('./files/reading_file_example.txt') as f:
    #splitlines(), otra forma de obtener todas las lineas
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)


