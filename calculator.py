command = input('Введите операцию: ')
while command != 'exit':
    if command == '+':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a+b)
    elif command == '-':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a-b)
    elif command == '*':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a*b)
    elif command == '/':
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        print(a/b)
    else:
        command = input('Неверная команда, введите еще раз: ')
    command = input('Введите операцию: ')