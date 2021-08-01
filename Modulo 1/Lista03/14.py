from random import randint
can1, can2, can3, can4, nul, bran = 0, 0, 0, 0, 0, 0
vot = randint(1,20000)
for i in range(0,vot):
    voto = randint(1,6)
    if voto == 1:
        can1 += 1
    if voto == 2:
        can2 += 1
    if voto == 3:
        can3 += 1
    if voto == 4:
        can4 += 1
    if voto == 5:
        nul += 1
    if voto == 6:
        bran += 1
    Total = can1+can2+can3+can4
print('Votos Cand. 1: {}\nVotos Cand. 2: {}'.format(can1, can2))
print('Votos Cand. 3: {}\nVotos Cand. 4: {}'.format(can3, can4))
print('Votos Nulos: {}\nVotos em Branco: {}'.format(nul, bran))
print('Percentural Nulos e Brancos: {:.1f}%'.format(((nul+bran)/(Total+nul+bran))*100))
