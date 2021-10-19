import math
import random

names = [
    'Аксёнов Федор Антонинович',
    'Козлова Василиса Руслановна',
    'Моисеев Соломон Протасьевич',
    'Кулакова Венера Владиславовна'
]

math_points = list(random.randint(1, 100) for i in range(len(names)))
russian_points = list(random.randint(1, 100) for i in range(len(names)))
informatics_points = list(random.randint(1, 100) for i in range(len(names)))

seq = list(zip(names, math_points, russian_points, informatics_points))
print(seq)
