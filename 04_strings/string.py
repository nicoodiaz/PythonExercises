empresa = 'Codificacion para todos'
print(empresa)
print(len(empresa))
print(empresa.upper())
print(empresa.lower())
empresa.capitalize()
empresa.title()
empresa.swapcase()
print(empresa[0:12])
print(empresa.index('Codificacion'))
print(empresa.replace('Codificacion', 'Python'))
print(empresa.split(' '))
empresa = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(empresa.split(','))
empresa = 'Codificacion para todos'
print(empresa.index('C'))
print(empresa.rfind('o'))
python = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('#'.join(python))
print(empresa.startswith('Codificacion'))
asd = '30DíasDePython'
print(asd.isidentifier())
sad = 'treinta_dias_de_python'
print(sad.isidentifier())