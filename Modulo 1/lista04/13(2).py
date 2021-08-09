
sal_min = float(input("R$"))
quant_enr = float(input("Quilowatt: "))
watts=sal_min/10000 * 7
print(f"""Valor do quilowatt: {watts:.2f}
Valor a pagar: {quant_enr*watts:.2f}
Novo valor com 10% de desconto: {quant_enr*watts * 0.9:.2f}""")
