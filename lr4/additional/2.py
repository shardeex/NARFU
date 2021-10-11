# 2. Создать список вещественных чисел. После серии подряд идущих
# повторяющихся чисел вставить количество их повторений.


import random


numbers = [float(random.randint(1, 9))]
counter = 1
for i in range(99):
    new_i = float(random.randint(1, 9))
    if new_i == numbers[-1]:
        counter += 1
    else:
        if counter > 1:
            numbers.append(counter)
            counter = 1
    numbers.append(new_i)
    
print(numbers)