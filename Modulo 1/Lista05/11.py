A, B = [int(input("digite um numero: ")) for x in range(0, 2)]
while True:
    if B > A:
        break
    A = A - B
print(A)
