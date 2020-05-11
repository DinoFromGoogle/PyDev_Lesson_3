f = open('text.txt', 'r', encoding='UTF8')  # получени доступа к текстовому файлу
fr = f.read()                               # приведение IO-объекта к типу str

# переменная для записи текста без знаков пунктуации
new_string = ""
# переменная, в которой содержится знак переноса
# строки - будет участвовать в условии
n = '\n'


# в тексте присутствуют символы дефис и тире
данное обстоятельство помогает нам избавиться
от тире между словами
defis = (chr(45))
dash = (chr(8212))

space = (chr(32))
line_break = (chr(10))


for i in fr:
    if i == n:
        i = ' '
    if i.isidentifier() or i == ' ' or i == defis:
        new_string += i

new_string = new_string.replace("  ", " ")
new_string_to_list = new_string.split(" ")

for i in new_string_to_list:
    print(i)


