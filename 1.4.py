mas = []
name = ''

while name != 'Конец':
    name = input('Напишите имя/Фамилию ')
    mas.append(name)

del mas[-1]
    
print(mas)

del_ = input('Какое имя/фамилию вы хотите удалить ')
index0 = 0
index1 = 0
new_mas = []

for r in mas :
    index0 += 1 


while index1 < index0:
    if mas[index1] != del_:
        new_mas.append(mas[index1])
    index1 += 1

mas = new_mas

  
 
print(mas)






