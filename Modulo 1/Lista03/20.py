div = 0
res = 0

x = int(input('Digite o valor de x: '))

for pot in reversed(range(1, 26)):
    div += 1
    if pot % 2 == 0:
        print(' -', '{}^{}/{}'.format(x, pot, div), end='')
        res -= x ** pot / div
    else:
        print(' +', '{}^{}/{}'.format(x, pot, div), end="")
        res += x ** pot / div

print('\nResultado = {:.5f}'.format(res))
