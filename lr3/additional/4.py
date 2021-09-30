# 1. Вывести на экран с применением операторов цикла

# а) в этой букве я вообще не понял зависимость, потому немного меняю правила...
# если кто-то объяснит, как и почему тут меняется, исправлю
for i in range(5):
    l = i
    for j in range(i+1):
        print(l, end=' ')
        l -= 1
    print()
print()

# б) тоже довольно костыльное решение
for i in range(5):
    l = i + 6 + 1
    for j in range(5-i):
        if j == 4-i:
            l = 2
        elif j == 1:
            l -= 1+2*i
        else:
            l -= 1
        print(l, end=' ')
    print()
print()

# в) 
for i in range(5):
    l = 30 - i
    for j in range(i+1):
        print(l, end=' ')
        l += 1
    print()
print()

# г)
for i in range(5):
    l = 20 - i
    for j in range(5-i):
        print(l, end=' ')
        l += 1
    print()
print()