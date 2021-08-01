x = 20
t1=0
t2=1
t3=1
c = 2
print('Voce escolheu o valor de {} números sua sequencia é: '.format(x))
if x >= 2:
    print('{}, {}'.format(t1, t2), end='')
elif x == 1:
    print("{}".format(t1))
while c < x:
    t3 = t1 + t2
    print(', {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
