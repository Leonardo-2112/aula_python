# Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses
#dois números, a multiplicação, a divisão inteira e o resto da divisão inteira.

#Exercício 4
"""
num1 = int (input("Digite um número:"))
num2 = int (input ("Digite outro número: "))
soma=num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"A soma é:{soma}")
print(f"A subtração é: {subtracao}")
print(f"A multiplicação é:{multiplicacao}")
print (f"a divisão é:{divisao}")
"""

#Exercício 5
"""

x = int(input("Digite um número: "))
y = int(input("Digite a potência do número: "))

valor = x ** y
print(f"O valor final é: {valor}")
"""

#Exercício 7
"""

num = int(input("Digite o número inteiro de 0 a 99: "))
dig_dez = num // 10
dig_uni = num % 10

print(f"O digito das dezenas é {dig_dez}, e o digito das unidades é {dig_uni}")
"""

#Exercício 9
"""

preco_prod = float(input("digite o valor do produto: "))
desc = float(input("Digite o desconto em %: "))
valor_desc = preco_prod * desc /100
preco_final = preco_prod - valor_desc
print(f"O valor descontado foi: {valor_desc}")
print (f"O valor final do produto é: {preco_final}")

"""

# Exercício 12
"""num = int(input("Digite o RM de 5 dígitos: "))
soma = 0

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

print("A soma vale", soma)"""



"""Exercício 11

valor = float (input("Valor da compra: "))
print("1 - dinheiro ou cheque, 10% de desconto")
print("2 - cartão de crédito, 5% de desconto")
print("3 - 2x o preço normal")
print("4 - 4x acréscimo de 7%")
forma_pgto = int(input("escolha uma das opções de pagamento acima: "))

match forma_pgto:
    case 1:
        desc = valor * 0.1
        print(f"O desconto foi de {desc}, você pagará {valor - desc}")
    case 2:
        desc = valor * 0.05
        print(f"O desconto foi de {desc}, você pagará {valor - desc}")
    case 3:
        parcela = valor /2
        print(f"Você pagará 2 x {parcela}")
    case 4:
        acrescimo = valor *0.07
        parcela = (valor + acrescimo) /4
        print(f"O valor do produto será de {valor + acrescimo} em 4x {parcela}")
    case _:
        print("Forma de pagamento inválida")
    """


