x = [int(input()) for x in range(30)]
a = int(input())
y= 0
for i in range(30):
    y[i]= x[i] * a
    print(f"o produto de {x[i]} x {a} = {y[i]} ", end=" ")
    if y[i] % 2 == 0:
        print("que é par")
    else:
        print("que é impar")
