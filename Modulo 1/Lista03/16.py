from random import randint
sim, nao, Fsim, Mnao = 0, 0, 0, 0
for i in range (0, 2000):
    vot = randint(1, 2)
    sex = randint(1, 2)
    if vot == 1:
        sim += 1
    if vot == 2:
        nao += 1
    if vot == 1 and sex == 2:
        Mnao += 1
    if vot == 2 and sex == 1:
        Fsim += 1
print('Votos SIM: {}\nVotos NÃO: {}'.format(sim, nao))
print('Fem. SIM: {}\nMasc. NÃO: {}'.format(Fsim, Mnao))
