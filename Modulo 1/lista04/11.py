#Criar um algoritmo que leia um valor de hora (hora:minutos) e informe (calcule) o total de minutos que se passaram desde o início do dia (0:00h).
h = str(input("escreva horas e minutosno fomato(0:00): "))
if len(h) <= 4:
    horas = int(h[0])
    minutos = int(h[2] + h[3])
elif len(h) <= 5:
    horas = int(h[0] + h[1])
    minutos = int(h[3] + h[4])
if minutos >= 60 or horas >= 24:
    print("horario invalido")
Total= minutos+(horas*60)
print(f"passaram {Total} minutos ")
