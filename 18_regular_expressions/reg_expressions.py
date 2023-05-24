import re


txt = 'Me encanta el lenguaje Python and SQL'
match = re.match('Me encanta el lenguaje', txt, re.I)
print(match)

#Podemos obtener la posicion del comienzo y final de la tupla usando span
span = match.span()
print(span) #(0, 22)


#En este caso, el patron que buscamos no inica en el texto que le pasamos, nos devuelve None
txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None


#Con search() se puede hacer una busqueda mas profunda, no solamente que coincida con el comienzo del texto
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match = re.search('first', txt, re.I)
print(match)
span = match.span()
print(span) #(100, 105)

#findall(), Esta funcion busca el patron en toda la cadena y devuelve todas las coincidencias en forma de lista
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Eso regresa una lista
matches = re.findall('language', txt, re.I)
print(matches)

#sub(), con esta funcion lo que podemos hacer es reemplazar un pedazo de una cadena
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)

#Otro ejemplo mas, la siguiente cadena, contiene el signo '%', lo que dificulta la lectura
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

#split(), Se dividen las cadenas y se las guarda en una lista nueva
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))

#Aqui se declara una variable de cadena y se le dice que la busque
#En este caso, solo encontrara coincidencias con 'apple' en minuscula
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)
#Para que tambien busque con mayuscula, debemos pasarle un "flag", en este caso como tercer parametro (re.I)
matches = re.findall(regex_pattern, txt, re.I)
print(matches)