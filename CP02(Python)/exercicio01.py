quantidade = int(input("Digite a quantidade de produtos: "))

maior_aumento_reais = 0
maior_aumento_percentual = 0

for i in range(quantidade):
    preco_atual = float(input("Digite o preco atual do produto: "))
    preco_reajustado = float(input("Digite o preco reajustado do produto: "))

    aumento_reais = preco_reajustado - preco_atual
    aumento_percentual = (aumento_reais / preco_atual) * 100

    if i == 0 or aumento_reais > maior_aumento_reais:
        maior_aumento_reais = aumento_reais

    if i == 0 or aumento_percentual > maior_aumento_percentual:
        maior_aumento_percentual = aumento_percentual

print(f"Maior aumento percentual: {maior_aumento_percentual:.2f}%")
print(f"Maior aumento em reais: R$ {maior_aumento_reais:.2f}")
