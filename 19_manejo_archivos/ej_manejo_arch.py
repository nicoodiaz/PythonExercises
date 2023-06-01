import json

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

def more_languages(num_cnt):
    with open('./files/countries_data.json', encoding='utf-8') as f:
        data = json.load(f)
    
    idiomas = {}
    for dictt in data:
        idioma = tuple(dictt['languages'])
        if idioma in idiomas:
            idiomas[idioma] += 1
        else:
            idiomas[idioma] = 1
    
    idioma_mas_hablado = sorted(idiomas.items(), key = lambda x: x[1], reverse=True)

    idiomas_top = idioma_mas_hablado[:num_cnt]
    
    for idioma, cantidad in idiomas_top:
        print(f'{idioma}: {cantidad} hablantes')
        
more_languages(3)
