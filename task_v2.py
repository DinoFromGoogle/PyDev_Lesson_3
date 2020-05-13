import pymorphy2

text = open('text.txt', 'r', encoding='UTF8')
text = text.read()          # получаем текст из файла в виде строки

print("."*70 + '\n' + "ЗАДАЧА_1.....Методами строк очистить текст от знаков препинания" + '\n' + "."*70)

last_index = len(text)-1    # индекс завершающего символа в строке
text_clear = ''             # строчная переменная для записи обработанного строки

# текст может быть грамотно написан с точки зрения
# пунктуации, но при разбивке на слова могут возникать
# нежелательные условия, которые надо учесть
# могут быть перепутаны дефисы(chr(45)) и тире(chr(8212)) (в заданном тексте присутствуют оба типа символов)
# в тексте могут встречаться цифры (в середине текста между латинскими словами есть 1)

# условие для первого символа из строки
# иначе при индексе [i-1], где i = 0 будет
# обращение к последнему символу в строке
if text[0].isalpha():
    text_clear += text[0]

for i in range(1, last_index, 1):  # диапазон задан от второго до предпоследнего символа строки
    if text[i].isalpha():
        text_clear += text[i]
    elif text[i] == chr(45) and text[i-1].isalpha() and text[i+1].isalpha():      # символ дефиса
        text_clear += text[i]
    elif text[i] == chr(8212) and text[i-1].isalpha() and text[i+1].isalpha():    # символ тире
        text_clear += text[i]
    elif not text[i].isalpha() and text[i+1].isalpha():
        text_clear += " "  # chr(32)

# условие для последнего символа из строки,
# иначе IndexError: string index out of range
if text[last_index].isalpha():
    text_clear += text[last_index]
print(text_clear)   # очищенный от знаков препинания текст

print()
print("."*70 + '\n' + "ЗАДАЧА_2_3.....Сформировать лист со словами и выполнить лемматизацию" + '\n' + "."*70)

# приведение строки со словами к списку слов
# через разделение пробелами
text_list = text_clear.split()  # если поставить знак пробела как аргумент - пробел в начале войдёт в список

# приведение к нижнему регистру - методы из загруженной библиотеки
# pymorphy2 распознают строки в нижнем регистре
text_list = list(map(lambda x: x.lower(), text_list))
print(f"{len(text_list)} - количество слов в тексте, в том числе иностранных, в том числе предлогов, союзов, частиц")

morph = pymorphy2.MorphAnalyzer()   # создание объекта для проведния морфологического анализа
text_list_lemma = []                # пустой список для записи нормальных форм слов
part_of_speech = ["CONJ", "NPRO", "PREP", "INTJ", "PRCL"]   # обозначения частей речи, которые надо исключить

for i in range(len(text_list)):     # цикл для проведения лемматизации и отбрасывания предлогов, частиц, союзов
    temp = morph.parse(text_list[i])[0]
    if temp.tag.POS in part_of_speech:
        continue
    text_list_lemma.append(temp.normal_form)

text_list_lemma.sort()
text_words = dict.fromkeys(text_list_lemma, 0)      # получение словаря с ключами по нормальным формам слов из текста

for i in text_words:        # цикл для записи количества повторений слова в словарь
    text_words[i] = text_list_lemma.count(i)

print(f'{len(text_words)} - количество разных слов в тексте, исключая предлоги, союзы, частицы')
print(text_words)
print()
# for i in text_words:
#     print(f'{i}....{text_words[i]}')

print("."*70 + '\n' + "ЗАДАЧА_4.....Вывести 5 наиболее часто встречающихся слов" + '\n' + "."*70)

words_sorted = list(text_words.items())
words_sorted.sort(key=lambda x: x[1])
words_sorted.reverse()
for i in range(5):
    print(f'{words_sorted[i][0]} \t---\t {words_sorted[i][1]}')
