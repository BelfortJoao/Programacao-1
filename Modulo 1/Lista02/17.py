Salario = float(input("Informe o Salário: "))
Prest_Val = float(input("Informe o valor da prestação: "))
if Prest_Val > ((Salario/100)*30):
    print("O emprestimo não pode ser concedido")
else:
    print("O emprestimo pode ser concedido")
