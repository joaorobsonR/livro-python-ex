cont = soma = maior = menor = 0
while True:
    n = int(input('digite um numero: '))
    if n <= 0:
        break
    if cont == 0:
        maior = menor = n
    if maior < n:
        maior = n
    elif menor > n:
        menor = n
    soma += n
    media = soma / n
    cont += 1

print('maior valor = {} menor valor = {}'.format(maior, menor))
print('soma = {}, media = {}'.format(soma, media))

