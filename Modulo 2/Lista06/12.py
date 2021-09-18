x = [int(input()) for x in range(10)]
tot=0
for i in range(10):
    tot += x[i]
for i in range(10):
    if x[i] > tot/10:
        print(x[i])
