try:
    a = int(input('digite um numero: '))
    b = int(input('digite um numero: '))
    r = a/b
    print('o resultado é r = %.1f' % r)
except ZeroDivisionError:
    print('não é possivel calcular a divisão')
except ValueError:
    print('digite valores inteiros')

