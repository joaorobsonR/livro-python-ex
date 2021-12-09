cont = 1
while True:
    try:
        n = int(input('digite um numero maior ou igual a 100: '))

    except ValueError:
        print('digite um numero inteiro!')

    else:
        if n < 100:
            print('ERRO, digite um numero maior que 100!')

    finally:
        print('\n')

    if n >= 100:
        break

while True:
    if cont == n:
        break
    if cont % 2 == 0:
        print(' → {}'.format(cont), end='')
    cont += 1

print('\033[31m fim\033[m')
