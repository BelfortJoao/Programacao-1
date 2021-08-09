Guarda = -(float('inf'))
Guarda_m = float('inf')
for i in range(0, 10):
    x = int(input())
    if x > Guarda:
        Guarda = x
    elif x < Guarda_m:
        Guarda_m = x
print(f"Menor: {Guarda_m}")
print(f"Maior: {Guarda}")
