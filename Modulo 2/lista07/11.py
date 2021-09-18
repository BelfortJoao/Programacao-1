x = [int(input()) for x in range(15)]
for i in range(15):
    if x[i] <0:
        x[i]=-1
print(x)