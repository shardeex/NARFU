number = int(input('введите натуральное число: '))
base = int(input('введите основание системы счисления: '))

if base < 2 or base > 16:
    print('основание степени должно быть от 2 до 16.')
    quit()

def converting(number, base):
    if number < base:
        return str(number)
    else:
        return converting(number // base, base) + str(number % base)

print(converting(number, base))