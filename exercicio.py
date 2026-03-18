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
