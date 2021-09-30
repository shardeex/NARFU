# 2. Два натуральных числа называются дружественными, если каждое из них
# равно сумме всех делителей другого (само другое число в качестве делителя
# не рассматривается). Найти все пары натуральных дружественных чисел,
# меньших 50 000.

friendly = []

for i in range(1, 50000):
    j = 0
    for x in range(1, i//2 + 1):
        if i % x == 0:
            j += x
    if j:
        compare_i = 0
        for x in range(1, j // 2 + 1):
            if j % x == 0:
                compare_i += x
        if compare_i == i and i != j:
            pair = min(i, j), max(i, j)
            if not pair in friendly:
                friendly.append(pair)
                print(f'найдена пара дружественных чисел: {pair[0]} и {pair[1]}')




