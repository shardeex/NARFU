# Дан текст, состоящий из количества строк текста и самого текста. Вывести на
# экран самое длинное слово. Для реализации используйте словари.

# словари не нужны...

text = "Короче представляете случилось такое непонятно что но вот знаете это очень круто \
и вообще довольно забавно просто самое интересное то что ну вот такое вот случилось потому \
что такого по идее не должно вообще быть но вот так получилось я в шоке Блин просто ужас я \
блин в полнейшем шоке и сейчас Вам расскажу Что же такое такое ТАКОЕ случилось жесть просто"

print(sorted(list([word.casefold() for word in text.split()]), key=lambda word: len(word))[-1])