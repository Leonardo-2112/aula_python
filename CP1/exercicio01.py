consumo_passado = float(input("Digite o consumo de água do mês passado (em metros cubicos): "))
consumo_atual = float(input("Digite o consumo de água do mês atual (em metros cubicos): "))

if consumo_atual <= 20:
    preco_por_metro = 2.0
elif consumo_atual <= 35:
    preco_por_metro = 3.50
elif consumo_atual <= 50:
    preco_por_metro = 5.50
else:
    preco = 7

valor = consumo_atual * preco_por_metro

if consumo_atual < consumo_passado:
    print(f"Valor do consumo: R$ {valor}")
    print(f"Desconto: R$ {valor * 0.15}")
    print(f"Valor final da conta: R$ {valor - (valor * 0.15)}")

elif consumo_atual > consumo_passado:
    print(f"Valor do consumo: R$ {valor}")
    print(f"Multa: R$ {valor * 0.10}")
    print(f"Valor final da conta: R$ {valor + (valor * 0.10)}")

