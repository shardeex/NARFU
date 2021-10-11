# 16. Создать список 11, 22, 33, ..., nn. Использовать генератор.

numbers = list([int(str(i)*2) for i in range(100)])

print(numbers)