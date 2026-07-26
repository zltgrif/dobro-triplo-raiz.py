import math

num = int(input('Digite um número: '))

op = input('Deseja calcular o dobro deste número? (s/n)')

if op == 's':
    dobro = num * 2
    print('O dobro de {} é: {}'.format(num, dobro))

else:
    print('Operação cancelada')

op = input('Deseja calcular o triplo deste número? (s/n)')

if op == 's':
    triplo = num * 3
    print('O triplo de {} é {}'.format(num, triplo))

else:
    print('Operação cancelada')

op = input('Deseja calcular a raíz deste número? (s/n)')

if op =='s':
    raiz = math.sqrt(num)
    #raiz = num ** (1/2)
    print('A raíz quadrada de {} é {}'. format(num, raiz))

else:
    print('Operação cancelada')