x = int(input())
if 0 <x< 500:
    print("nenhum credito")
elif 501 <x<1000:
    print(f"O seu credito é de R${X*0.3}\n o saldo é de R${x*1.3}")
elif 1001 < x <3000:
    print(f"O seu credito é de R${X * 0.4}\n o saldo é de R${x * 1.4}")
elif x < 3001:
    print(f"O seu credito é de R${X * 0.5}\n o saldo é de R${x * 1.5}")
