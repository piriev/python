print('Поле чудес! \nЧтобы выиграть, Вы должны отгадать слово')
python = 'python'
#python = ['p','y','t','h','o','n']
word = ['*','*','*','*','*','*']
print('Первое слово(на английском языке) - название языка программирования, разработанный Гвидо ван Россум')
while '*' in word:
    letter = input('Назовите букву: ')
    if letter in python:
        print('\nВерно!')
        if letter == 'p':
            del word[0]
            word.insert(0,'p')
        if letter == 'y':
            del word[1]
            word.insert(1,'y')
        if letter == 't':
            del word[2]
            word.insert(2,'t')
        if letter == 'h':
            del word[3]
            word.insert(3,'h')
        if letter == 'o':
            del word[4]
            word.insert(4,'o')
        if letter == 'n':
            del word[5]
            word.insert(5,'n')
    elif letter == 'Показать слово':
        for elem in word:
            print(elem)
    else:
        print('\nНеверная буква! Попробуйте еще раз.')
print('Правильно! Вы победили!')