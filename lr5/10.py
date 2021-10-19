seq = ['Маша', 'Петя', 'Вася']
hsh = lambda i: hash(i)

seq = list(map(hsh, seq))
print(seq)