soma_maiores_50 = 0
quantidade_menores_100 = 0
impares_consecutivos = 0

while impares_consecutivos < 3:
    numero = int(input("Digite um numero inteiro positivo: "))

    if numero > 50:
        soma_maiores_50 += numero

    if numero < 100:
        quantidade_menores_100 += 1

    if numero % 2 != 0:
        impares_consecutivos += 1
    else:
        impares_consecutivos = 0

print(f"Soma dos numeros maiores que 50: {soma_maiores_50}")
print(f"Quantidade de numeros menores que 100: {quantidade_menores_100}")
