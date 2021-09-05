x = [int(input()) for x in range(10)]
a = int(input())
for i in range(10):
    if a > x[i]:
        print(x[i], end=", ")