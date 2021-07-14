# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку
#
# TODO: your code here
#
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

# Вариант 2. re.sub()

import re

new_text = re.sub('[^A-Za-z0-9]+', ' ', text+ ' ')
text_tuple = tuple(new_text)
count = 0
result = 0
for le in text_tuple:
    if le != ' ':
        count = count + 1
    elif count > 7:
        result = result + 1
        count = 0
    else:
        count = 0

print(result," Слов больше 7 символов.")

# Вариант 3. len()

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
