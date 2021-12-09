while True:
    try:
        n = int(input('digite um numero: \033[32mdigite 0 para parar: \033[m'))
        if n == 0:
            print('o numero digitado é neutro, \033[32mfim\033[m')
            break
        elif n > 0:
            print('o numero digitado é positivo {}'.format(n))
        else:
            print(f'o numero digitado é negativo {n}')

    except ValueError:
        print('digite um numero inteiro')
