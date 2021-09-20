# Дано пятизначное число. Найти число, получаемое при прочтении его цифр справа
# налево.

number = input('введите число: ')
for i in range(len(number)):
    print(number[len(number)-i-1], end='')