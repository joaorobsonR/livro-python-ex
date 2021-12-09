soma = 0
print('digite um numero aleatório,\n'
                  'negativo ou positivo, apenas\n'
                  'os positivos serão somados. ')
while True:
    n = int(input(''))

    if n == 999:
        print('FIM')
        break
    elif n >= 0:
        soma += n

print(f'a soma dos numeros positivos é {soma}')
