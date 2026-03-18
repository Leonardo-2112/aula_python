num_a = float(input("Número a: "))
op = input("Operador (+ - * /): ")
num_b = float(input("Número b: "))

if op == '+':
    print(num_a + num_b)
elif op == '-':
    print(num_a - num_b)
elif op == '*':
    print(num_a * num_b)
elif op == '/':
    if num_b != 0:
        print(num_a/num_b)
    else:
        print ("Não existe divisão por 0")