from random import randint
from time import sleep

cont = 0
while True:
    a = int(input('digite um numero de 0 até 100: '))
    b = randint(0, 100)
    print('o computador está escolhendo..')
    sleep(3)
    if a > b:
        print('vc venceu {} contra {}'.format(a, b))
    elif a < b:
        print(f'vc perdeu {b} contra {a}')
        break
    else:
        print(f'deu empate {a} conta {b}')
    cont += 1

print(f'vc venceu um total de {cont} vezes')
