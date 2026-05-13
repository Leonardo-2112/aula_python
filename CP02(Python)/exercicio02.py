cedula = int(input("Digite o valor da cedula: "))
moeda_a = int(input("Digite o valor de uma moeda: "))
moeda_b = int(input("Digite o valor da outra moeda: "))

possivel = False
quantidade_a = 0
quantidade_b = 0

for qtd_a in range(cedula // moeda_a + 1):
    restante = cedula - qtd_a * moeda_a

    if restante % moeda_b == 0:
        possivel = True
        quantidade_a = qtd_a
        quantidade_b = restante // moeda_b
        break

if possivel:
    print(f"Possivel: {quantidade_a} moeda(s) de {moeda_a} e {quantidade_b} moeda(s) de {moeda_b}")
else:
    print("Nao e possivel fazer a troca")
