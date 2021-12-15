# Напишите функцию max_length_word(file), которая открывает для чтения файл 
# file и возвращает из него слово с максимальной длиной или список таких 
# слов, если их несколько.
# Для выполнения данного задания создайте файл «title.txt», куда запишите 
# следующий текст:

import os

def max_length_word(file):
    max_words = ['']
    with open(file, encoding='utf8') as f:
        while (line := f.readline()):
            word = ''
            for lt in line:
                if lt.isalpha():
                    word += lt
                else:
                    if len(word) > len(max_words[0]):
                        max_words = [word]
                    elif len(word) == len(max_words[0]):
                        max_words.append(word)
                    word = ''
    
    return max_words

print(*max_length_word('lr8\\title.txt'))