# Даны два списка чисел, введенных с клавиатуры. Определить, сколько и каких 
# чисел одновременно встречается в двух списках.

first_set = set(map(int, input('введите первый список: ').split()))
second_set = set(map(int, input('введите второй список: ').split()))

print(f'кол-во общих чисел: {len(first_set.intersection(second_set))}, {first_set.intersection(second_set)}')