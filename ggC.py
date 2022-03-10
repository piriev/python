#veg = ['помидор','огурец','капуста']
#newVeg1 = input('Добавьте к списку первый овощ: ')
#newVeg2 = input('Добавьте к списку второй овощ: ')
#veg.append(newVeg1)
#veg.append(newVeg2)
#print(veg)

commands = ['игры','погода','новости','добавить','удалить', 'команды', 'выход']
command = input('Введите команду: ')
while(command != commands[6]):
    if command == commands[3]:
        commands.append(input('Введите новую команду: '))
    elif command == commands[4]:
        commands.remove(input('Введите название команды: '))
    elif command == commands[5]:
        for elem in commands:
            print(elem)
    command = input('Введите команду: ')