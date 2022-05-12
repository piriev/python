pole =  [['O','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*'],
         ['*','*','*','*','*','*','*','*','*','*']]
for stroka in pole:
    for kletka in stroka:
        print(kletka,'',end='')
    print()
placeA = 0
placeB = 0
while True:
    pole[placeB][placeA] = '*'
    placeNew = input('Введите команду: ')
    if placeNew == 'right':
        if placeA < 9:
            placeA += 1
            pole[placeB][placeA] = 'O'
        else:
            placeNew = input('Нельзя направо! Повторите попытку: ')
    if placeNew == 'left':
        if placeA > 0:
            placeA -= 1
            pole[placeB][placeA] = 'O'
        else:
            placeNew = input('Нельзя налево! Повторите попытку: ')
    if placeNew == 'up':
        if placeB > 0:
            placeB -= 1
            pole[placeB][placeA] = 'O'
        else:
            placeNew = input('Нельзя на вверх! Повторите попытку: ')
    if placeNew == 'down':
        if placeB < 9:
            placeB += 1
            pole[placeB][placeA] = 'O'
        else:
            placeNew = input('Нельзя вниз! Повторите попытку: ')
    for stroka in pole:
        for kletka in stroka:
            print(kletka,'',end='')
        print()