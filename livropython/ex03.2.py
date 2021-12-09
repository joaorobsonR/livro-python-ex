def fib(x):
    if x < 2:
        return x
    else:
        return fib(x-1) + fib(x-2)


n = int(input('digite um termo da sequencia fibonaci: '))
a = 0
b = 1
i = 0
while n < 2:
    print('\033[32mdigite um termo maior ou igual a dois\n'
          'pois o primeiro e segundo termo são\n'
          '0 e 1 respectivamente.\033[m')
    n = int(input('digite um termo da sequencia fibonaci: '))

print('0, 1,', end='')
while i < n - 2:
    c = a + b
    print(' {},'.format(c), end='')
    a = b
    b = c
    i += 1

print(' fim')
