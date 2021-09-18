import random
M2 = M3 = M1 = [[0 for i in range(4)] for y in range(4)]
for i in range(4):
    for j in range(4):
        M1[i][j] = random.randint(0, 10)
        M2[i][j] = random.randint(0, 10)
for i in range(3):
    for j in range(4):
        M3[i][j] = M1[i][j] + M2[i][j]
print(M3)
