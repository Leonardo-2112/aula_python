texto = input("Digite uma string: ")
nova_string = ""
vogais = "aeiou"

for caractere in texto:
    if caractere == " ":
        continue
    elif caractere.isdigit():
        nova_string += "*"
    elif caractere.lower() in vogais:
        nova_string += caractere.upper()
    elif caractere.isalpha():
        nova_string += caractere.lower()
    else:
        nova_string += caractere

print(nova_string)
print(nova_string[::-1])
