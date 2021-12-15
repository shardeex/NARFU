# Напишите функцию remove_braces(st), в которую передается строка st, 
# содержащая текст со словами в скобках, и которая возвращает этот текст без 
# слов в скобках. При этом нужно учесть, что самая последняя открывающая 
# скобка должна обязательно иметь после себя закрывающую.

def remove_braces(st):
    opened_braces = 0
    new_st = ''

    for lt in st:
        if lt == '(':
            opened_braces += 1
        elif lt == ')':
            opened_braces -= 1
        elif not opened_braces:
            new_st += lt
    
    return new_st

print(remove_braces('(арва) ыовоыт'))
print(remove_braces('(лишнее(лишнее))Шила в мешке не (лишнее(лишнее(лишнее)))утаишь'))