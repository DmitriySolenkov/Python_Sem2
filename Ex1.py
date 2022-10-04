string = str(input('Введите строку:'))
ch = str(input('Введите символ для поиска:'))
sym = ch[0]
count = 0
for i in string:
    if i == sym:
        count += 1
print(f'Символ {sym} встречается в строке {count} раз')
