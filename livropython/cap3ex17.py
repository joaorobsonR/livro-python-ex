from random import randint

cont = maior = menor = 0
n = int(input('digite um numero: '))

while True:
    comp = randint(-100, 100)
    if cont == n:
        break
    if comp < 0:
        continue
    if comp >= 0:
        if cont == 0:
            maior = menor = comp
        if maior < comp:
            maior = comp
        elif menor > comp:
            menor = comp
    cont += 1
    print(' → ', comp, end='')

print('\n')
print('o maior numero é {}'.format(maior))
print(f'o menor numero é {menor}')
