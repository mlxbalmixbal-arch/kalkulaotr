print('--------------------------------------')
print("крути калькулятор")
print('введи 2 числа и что с ними сделать')
print('--------------------------------------')
while True:
    num1 = float(input('Первое чиcло '))
    num2 = float(input('Второе число '))
    operation = input('Операция (+, -, *, **, /) ')
    if operation == '+':
        result = num1 + num2
        print(f'{num1} + {num2}', 'это будет', result)
    elif operation == '-':
        result = num1 - num2
        print(f'{num1} - {num2}', 'это будет', result)
    elif operation == '/':
        if num1 == 0:
            print('нельзя делить на ноль, другое число')
        elif num2 == 0:
            print('нельзя делить на ноль, другое число')
        else:
                result = num1 / num2
                print(f'{num1} / {num2}', 'это будет', result)
    elif operation == '//':
        if num1 == 0:
            print('нельзя делить на ноль, другое число')
        elif num2 == 0:
            print('нельзя делить на ноль, другое число')
        else:
                result = num1 // num2
                print(f'{num1} / {num2}', 'это будет', result)
    elif operation == '*':
        result = num1 * num2
        print(f'{num1} * {num2}', 'это будет', result)
    elif operation == '**':
        result = num1 ** num2
        print(f'{num1} ** {num2}', 'это будет', result)
    else:
        print('неправильно')
    print('новые числа?')
    ans = input('да или нет ')
    if ans == 'нет':
        print('пока')

        break
