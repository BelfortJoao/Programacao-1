# Escreva um algoritmo que leia do teclado dois números: divisor e dividendo. O algoritmo deve apresentar o quociente e o resto da divisão. Caso o valor do divisor seja zero, o algoritmo deve escrever “Divisão não permitida” e encerrar.
Dividendo = int(input("Dividendo: "))
Divisor = int(input("Divisor: "))
if Dividendo <= 0:
    print("Divisão não permitida")
else:
    Resto = Dividendo % Divisor
    Quociente = Dividendo // Divisor
    print("Resto: {} \nQuociente: {}".format(Resto, Quociente))