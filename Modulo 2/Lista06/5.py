x = [int(input(f"escreva a nota do aluno {x+1}: ")) for x in range(25)]
Tot=0
for i in range(25):
    Tot += x[i]
    Media = Tot/25
print(f"Media = {Media}")