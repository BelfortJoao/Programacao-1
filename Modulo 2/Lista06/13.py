w = [int(input()) for x in range(15)]
y = 0
z = 0
while True:
    for i in range(14):
        if w[i] <= w[i+1]:
            z += 1
        else:
            z = 0
            y = w[i]
            w[i] = w[i+1]
            w[i+1] = y
        print(z)
    if z > 14:
        break
print(w)