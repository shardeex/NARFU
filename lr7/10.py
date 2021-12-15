points = {}
students = []

with open('lr7\\10.txt', encoding='utf8') as file:
    k = int(file.readline())
    for st_str in file.readlines():
        student = ' '.join(st_str.split()[:-3])
        ex1, ex2, ex3 = map(int, st_str.split()[-3:])
        if min(ex1, ex2, ex3) >= 40:
            pts = ex1 + ex2 + ex3
            students += [student]
            if points.get(pts):
                points[pts].append(student)
            else:
                points[pts] = [student]

sorted_points_list = sorted(points, reverse=True)
allowed_students = []
min_points = 300

for pts in sorted_points_list:
    if len(allowed_students) + len(points[pts]) > k:
        break
    else:
        allowed_students += points[pts]
        min_points = pts

if students == []:
    print('?, не будет зачислено абитуриентов, все имею неудовлетвортельные оценки')
elif allowed_students == students:
    print('0, будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок')
elif allowed_students == []:
    print('1, количество абитуриентов, имеющих равный максимальный балл больше чем K')
else:
    print(min_points)
