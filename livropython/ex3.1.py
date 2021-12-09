from random import randint

cont = soma = 0
try:
    n = int(input('digite um numero: '))
    while True:
        if cont == n:
            break
        comp = randint(1, 50)
        print(' → ',comp, end='')
        soma += comp
        cont += 1
except ValueError:
    print('digite um valor inteiro')
print(' a soma dos valores é {}'.format(soma))

