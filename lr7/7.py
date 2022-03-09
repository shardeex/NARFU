print('а)')
with open('lr7\\7.txt', encoding='utf8') as file:
    for string in file.readlines():
        print(string[::-1].replace('\n', ''))
        # another_file.write(...)

print('\nб)')
with open('lr7\\7.txt', encoding='utf8') as file:
    for string in file.readlines()[::-1]:
        print(string[::-1].replace('\n', ''))
        # another_file.write(...)
