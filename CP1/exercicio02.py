login = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if login == "scott" and senha == "tiger":
    print("Autenticado com sucesso")
elif login == "walt" and senha == "disney":
    print("Autenticado com sucesso") 
elif login == "spock" and senha == "ncc1701":
    print("Autenticado com sucesso") 
else:
    print("Usuário ou senha inválidos")