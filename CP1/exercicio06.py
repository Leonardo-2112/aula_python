x = float(input("Digite a coordenada X: "))
y = float(input("Digite a coordenada Y: "))

if x == 0 and y == 0:
    print("Origem")
elif y == 0 and x != 0:
    print("Eixo X")
elif x == 0 and y != 0:
    print("Eixo Y")
elif x > 0 and y > 0:
    print("Quadrante 1")
elif x < 0 and y > 0:
    print("Quadrante 2")
elif x < 0 and y < 0:
    print("Quadrante 3")
elif x > 0 and y < 0:
    print ("Quadrante 4")