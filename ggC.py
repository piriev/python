#veg = ['помидор','огурец','капуста']
#newVeg1 = input('Добавьте к списку первый овощ: ')
#newVeg2 = input('Добавьте к списку второй овощ: ')
#veg.append(newVeg1)
#veg.append(newVeg2)
#print(veg)

jobList = ['купить продукты','поставить вещи в стирку']
command = input('Введите команду: ')
while command != 'выход':
    if command == 'добавить':
        jobList.append(input('Введите новую заметку: '))
    elif command == 'удалить':
        jobList.remove(input('Введите название заметки: '))
    elif command == 'редактировать':
        name = input('Введите название заметки: ')
        index = jobList.index(name)
        if name in jobList:
            jobList[index] = input('Введите новое название: ')
    elif command == 'список':
        for elem in jobList:
            print(elem)
    command = input('Введите команду: ')