# Напишите функцию delete_backspace (st), в которую передается строка st, со 
# спецсимволом «@» обозначающим удаление одного символа слева от спецсимвола, 
# и которая возвращает строку, очищенную от удаляемых символов и спецсимволом.

def delete_backspace(st):
    while '@' in st:
        pos = st.find('@')
        st = st[:pos-1] + st[pos+1:]
    
    return st

print(delete_backspace('пп@олс@кр@овт@оде@ец'))
print(delete_backspace('сварка@@@@@лоб@ну@'))