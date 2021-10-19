import random

def is_prime(number, div=None):
    if div == None:
        div = number - 1
    while div > 1:
        if number % div == 0:
            return False
        else:
            return is_prime(number, div-1)
    else:
        return True

number = random.randint(2, 1000)
print(number, is_prime(number))