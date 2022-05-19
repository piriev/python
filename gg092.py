pole =  [['O',' ',' ',' ','#','*','*','*','*','*'],
         ['#','#','#',' ','#','*','*','*','*','*'],
         ['*','*','#',' ','#','*','*','*','*','*'],
         ['*','*','#',' ','#','*','*','*','*','*'],
         ['#','#','#',' ','#','*','*','*','*','*'],
         [' ',' ',' ',' ','#','#','#','#','#','#'],
         [' ','#','#','#','#','#',' ',' ',' ',' '],
         [' ','#','#','#','#','#',' ','#','#',' '],
         [' ',' ',' ',' ',' ',' ',' ','#','#',' '],
         ['#','#','#','#','#','#','#','#','#','!']]
for stroka in pole:
    for kletka in stroka:
        print(kletka,'',end='')
    print()
placeA = 0
placeB = 0
while pole[9][9] != 'O':
    placeNew = input('Введите команду: ')
    if placeNew == 'right':
        if placeA < 9:
            if pole[placeB][placeA + 1] != '#': 
                pole[placeB][placeA] = ' '
                placeA += 1
                pole[placeB][placeA] = 'O'
            else:
                print('Нельзя направо!')
    if placeNew == 'left':
        if placeA > 0:
            if pole[placeB][placeA - 1] != '#':
                pole[placeB][placeA] = ' '
                placeA -= 1
                pole[placeB][placeA] = 'O'
            else:
                print('Нельзя налево!')
    if placeNew == 'up':
        if placeB > 0:
            if pole[placeB - 1][placeA] != '#':
                pole[placeB][placeA] = ' '
                placeB -= 1
                pole[placeB][placeA] = 'O'
            else:
                print('Нельзя на вверх!')
    if placeNew == 'down':
        if placeB < 9:
            if pole[placeB + 1][placeA] != '#':
                pole[placeB][placeA] = ' '
                placeB += 1
                pole[placeB][placeA] = 'O'
            else:
                 print('Нельзя вниз!')
    for stroka in pole:
        for kletka in stroka:
            print(kletka,'',end='')
        print()
print('Победа!')