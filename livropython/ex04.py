N = int(input('Digite N: '))
Cont = 0
i = 2
while i < N:
    R = N % i
    if R == 0:
        Cont += 1
    i += 1
if Cont == 0:
    print('{} é primo' .format(N))
else:
    print('{} não é primo'.format(N))

n = int(input('digite um numero: '))
d = 2
while d < n:
    r = n % d
    if r == 0:
        print('o numero {} não é primo'.format(n))
        break
    d += 1
else:
    print('o numero é {} primo'.format(n))
