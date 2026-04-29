#Usando a função que verifica se um número é perfeito ou não, escreva um programa que encontra todos os números perfeitos no intervalo de 1 a 5000
def perfeito(num: int) -> bool:
    div = 0
    num = 0
    while div < num:
        if num % div == 0:
            soma = soma + div
        div = div + 1
    if soma == num:
        return True
    else:
        return False
    numero = 1
    while numero <= 50000:
        if numero % 10000 == 0:
            print(numero)
        if perfeito(numero) == True:
            print(numero)
        numero = numero + 1