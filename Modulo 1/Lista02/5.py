Dividendo= int(input("Qual o dividendo? "))
Divisor= int(input("Qual o divisor? "))
Quociente = Dividendo//Divisor
Resto = Dividendo%Divisor
if Divisor <= 0:
    print("Divisão não permitida")
else:
    print("Resto= {} \nQuociente= {}".format(Resto,Quociente))



