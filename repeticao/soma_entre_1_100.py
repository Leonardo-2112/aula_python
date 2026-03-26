n = int(input("Digite um número inteiro positivo: "))

while n < 0:
    n = input("Erro! Digite um número inteiro positivo: ")
soma = 0;
i = 1
while i <= n:
    soma = soma + i
    i = i + 1
print("Valor da soma ", soma)