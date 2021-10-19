from functools import reduce
sentences = ['научиться плести рыболовные сети', 'обучать нейронные сети', 'паук ловит в сети мух']

print(reduce(lambda x, y: x + y.count('сети'), sentences, 0))