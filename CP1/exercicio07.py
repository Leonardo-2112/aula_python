valor = float(input("Digite o valor da compra: "))
tipo = int(input("Tipo de cliente (1-Comum, 2-VIP, 3-Premium): "))

desconto = 0

# Aplicar desconto
if tipo == 1:
    desconto = 0
elif tipo == 2:
    if valor > 100:
        desconto = valor * 0.05
elif tipo == 3:
    if valor > 500:
        desconto = valor * 0.15
    else:
        desconto = valor * 0.10

valor_final = valor - desconto

# Calcular frete
if valor_final < 200:
    frete = 25
else:
    frete = 0

total = valor_final + frete

print("Desconto:", desconto)
print("Frete:", frete)
print("Total a pagar:", total)