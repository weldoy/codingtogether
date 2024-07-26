def multiply():
    first = int(input('enter the first digit: '))
    second = int(input('enter the second digit: '))
    return first * second


def divide():
    first = int(input('enter the first digit: '))
    second = int(input('enter the second digit: '))
    if second != 0:
        return first/second
    else:
        return 'u cant divide by zero'


def plus():
    first = int(input('enter the first digit: '))
    second = int(input('enter the second digit: '))
    summ = first + second
    return summ


def minus():
    first = int(input('enter the first digit: '))
    second = int(input('enter the second digit: '))
    summ = first - second
    return summ


def calculate():
    print(
        '1 - minus\n',
        '2 - plus\n',
        '3 - divide\n',
        '4 - multiply\n')
    request = input('What is your req? :')
    if request == '1' or request == 'minus':
        return minus()
    elif request == '2' or request == 'plus':
        return plus()
    elif request == '3' or request == 'divide':
        return divide()
    elif request == '4' or request == 'multiply':
        return multiply()
    else:
        return 'bro, ti dolboeb. u menya nema takoy huini'


print(calculate())
