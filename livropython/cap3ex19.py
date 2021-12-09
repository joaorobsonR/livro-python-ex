from random import randint

cont = 0
while True:
    r = randint(0, 100)
    if r == 0 or cont == 50:
        break
    if r % 2 == 0:
        print(' → {}'.format(r), end='')
    elif r % 3 == 0:
        print(' → {}'.format(r), end='')
    cont += 1
