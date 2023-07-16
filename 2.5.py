sl = input('Напишите слова через пробел ') + ' '
slovo = ''
mas = []

for r in sl :
    if r == ' ':
        mas.append(slovo)
        slovo = ''
    else:
        slovo += r


print(mas)
     


