# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

# TODO: your code here
# Вариант 1. isalpha()

import string
text_char = tuple(text + ' ')
count = 0
result = 0
for char in text_char:
    if char.isalpha() == True:
        count = count + 1
    elif count > 7:
        result = result + 1
        count = 0
    else:
        count = 0
print(result, " Слов больше 7 символов.")

#Вариант 2. re-модуль для работы с регулярными выражениями

import re

new_text = list(re.sub(r'[^A-Za-z0-9]', ' ', text + ' ')) # re.sub-ищет в тексте шаблон '[^A-Za-z0-9]' и заменяет на пробел.
count = 0
result = 0
for le in new_text:
    if le != ' ':
        count = count + 1
    elif count > 7:
        result = result + 1
        count = 0
    else:
        count = 0
print(result," Слов больше 7 символов.")

# Вариант 3. len() and re.sub()

import re

new_text = re.sub(r'[^A-Za-z0-9]', ' ', text + ' ')
lenght = len(new_text)
i=0
count = 0
result = 0
while i < lenght:
    if new_text[i] != " ":
        count = count + 1
    else:
        if count > 7:
            result = result + 1
        count = 0
    i += 1
print(result," Слов больше 7 символов.")
