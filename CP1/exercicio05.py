a = 0
b = 0
nulo = 0
branco = 0

while True:
    print("1 - Candidato A")
    print("2 - Candidato B")
    print("3 - Nulo")
    print("4 - branco")
    print("0 - Para Sair")
    voto = int(input("Digite seu voto: "))
    
    if voto == 0:
        break
    elif voto == 1:
        a += 1
    elif voto == 2:
        b += 1
    elif voto == 3:
        nulo += 1
    elif voto == 4:
        branco += 1
    else:
        print("Voto inválido")

print("Candidato A:", a)
print("Candidato B:", b)
print("Nulos:", nulo)
print("Brancos:", branco)