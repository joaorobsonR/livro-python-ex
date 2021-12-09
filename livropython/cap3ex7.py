try:
    hora = int(input('digite as horas trabalhadas do mês: '))
    extra = int(input('digite as horas extras do mês: '))
    salario = hora * 30 + extra * 60

except ValueError:
    print('digite um numero inteiro!')

print(f'o salario do funcionario no mês será {salario}')
