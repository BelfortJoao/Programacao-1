cont_par = 0
cont_imp = 0
for x in range(0, 2):
    num = int(input())
    if num % 2 == 0:
        cont_imp += 1
    else:
        cont_par += 1
print(f"impar: {cont_imp}")
print(f"par: {cont_par}")
