import random
M1 = [[0 for i in range(10)] for y in range(5)]
M = 0
for i in range(5):
    for j in range(10):
        M1[i][j] = random.randint(120, 200)
i = 0
while True:
    for j in range(10):
        if M1[i][j] > M:
            M= M1[i][j]
    print(M)
    i += 1
    M = 0
    if i == 5:
        break
print(M1)
