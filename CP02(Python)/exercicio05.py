palavra = input("Digite uma palavra: ")

for i in range(1, len(palavra) + 1):
    print(palavra[:i])

for i in range(len(palavra) - 1, 0, -1):
    print(palavra[:i])
