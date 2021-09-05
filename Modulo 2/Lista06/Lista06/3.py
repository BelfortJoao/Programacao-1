x = [int(input()) for x in range(20)]
y= 0
for i in range(19):
    print(x[i], end=", ")
print(x[19], ".")
for i in range(10):
    y = x[i]
    x[i] = x[19-i]
    x[19-i]= y
print(x)
