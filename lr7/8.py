f1 = open('lr7\\8_1.txt', encoding='utf8')
f2 = open('lr7\\8_2.txt', encoding='utf8')

lines1 = f1.readlines()
lines2 = f2.readlines()

if lines1 == lines2:
    print('Не отличаются!')

for i in range(len(lines1)):
    if lines1[i] != lines2[i]:
        print(f'Отличаются, начиная со строки №{i+1}')
        exit()

