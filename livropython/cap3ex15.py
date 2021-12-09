try:
    max = int(input('digite um numero maximo: '))
    min = int(input('digite um numero minimo: '))
    print('\n')
    if max < min:
        print('o valor digitado não está na ordem: ')
        max, min = min, max
    elif max == min:
        print('os numeros digitados são iguais!')
except ValueError:
    print('o valor digitado não está correto!')

while min <= max:
    resto = max % 5
    if resto == 0:
        print(max, '→' , end='')
    max -= 1

print('FIM')
