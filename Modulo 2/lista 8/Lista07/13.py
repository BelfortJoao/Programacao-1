import random
M1 = [[0 for i in range(3)] for y in range(5)]
S = [0 for i in range(3)]
for i in range(3):
    for j in range(5):
        M1[i][j] = random.randint(0, 10)
for i in range(3):
    for j in range(4):
        S[i] += M1[i][j]
print(S)
