seq = ['катя', 'маша', 'таня', 'саша']
cap = lambda i: i.capitalize()

seq = list(map(cap, seq))
print(seq)