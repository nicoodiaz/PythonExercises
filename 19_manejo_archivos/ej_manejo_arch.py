def count_lines_words(rute):
    with open(rute) as f:
        lines = f.read().splitlines()
    count_line = 0
    count_word = 0
    for i in lines:
        count_line += 1
        for x in i:
            count_word += 1
    print('Aqui se cuenta las lineas de un txt:')
    print(count_line)
    print('Aqui se cuenta las palabras de cada linea:')
    print(count_word)



count_lines_words('./files/obama_speech.txt')