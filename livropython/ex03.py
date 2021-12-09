soma = cont = 0
while True:
    x = int(input('digite um numero: '))
    if x == 999:
        break
    elif x < 0:
        continue
    else:
        soma += x
        cont += 1

print('o valor da soma dos numeros digitados é {}'.format(soma))
print(f'a quantidade de numeros digitados é {cont}')
