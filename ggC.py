inventory = ['Меч','Щит']
print('Чтобы посмотреть инвентарь, введите команду - Инвентарь')
command = input()
if command == 'Инвентарь':
    for elem in inventory:
        print(elem)
print('\nВы находитесь в замке. Открывая дверь, Вы заметили, что есть еще две двери. \nПервая дверь справа, вторая слева.')
command = input('Какую дверь выберите?\n')
while (command != 'Первую') and (command != 'Вторую') and (command != 'Выход'):
    command = input('Неверная команда! Повторите попытку: ')
if command == 'Первую':
    print('Рядом с дверью Вы видите канделябр с зажженным факелом. \nВозьмете его?')
    torch = input()
    while (torch != 'Да') and (torch != 'Нет'):
        torch = input('Неверная команда! Повторите попытку:')
    if torch == 'Да':
        inventory.append('Факел')
        print('(в инвентарь добавлен факел)')
    print('Зайдя внутрь, Вы заметили, что впереди длинный темный тоннель.')
    if 'Факел' in inventory:
        do1 = input('Использовать факел? ')
        if do1 == 'Да':
            inventory.remove('Факел')
            print('Вы осветили себе путь')
    print('Вы нашли золотую статуэтку и покинули замок. \nИгра окончена.')
if command == 'Вторую':
    print('Впереди летучие мыши.')
    command = input('Просто пройдете вперед?\n')
    while (command != 'Да') and (command != 'Нет'):
        command = input('Неверная команда! Повторите попытку: ')
    if command == 'Да':
        print('Летучие мыши напали на Вас, и Вы решили покинуть замок. \nИгра окончена')
    if command == 'Нет':
        command = input('Выберите предмет из своего инвентаря: ')
        while command != 'Меч' and command != 'Щит':
            command = input('Неверная команда! Повторите попытку: ')
        print('Вы пробились через летучих мышей и нашли сокровищницу с золотом. \nИгра окончена.')
if command == 'Выход':
    print('Вы покинули замок.\nИгра окончена')
    
