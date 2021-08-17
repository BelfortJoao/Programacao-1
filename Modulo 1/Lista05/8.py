m = int("inf")
M = -int("inf")
cont = 0
while True:
    n = int(input())
    if n == -1:
        break
    if n < m:
        m = n
    if n > M:
        M = n
print(f"Maior: {M}\nMenor:{m}")
