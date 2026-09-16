print("==============")
print("CALCULADORA")
print("==============")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

op = int(input("Escolha uma opção: "))

while op != 5:

    conta =[]

    if op == 1:
        print("Opção de SOMA selecionada")
        for i in range(2):
            ns = float(input(f"Digite o {i + 1}º numero: "))
            conta.append(ns)
        ad = conta[0] + conta[1]
        print(f"{conta[0]} + {conta[1]} = {ad}" )
        op = int(input("Escolha uma opção: "))


    elif op == 2:
        print("Opção de SUBTRAÇÃO selecionada")
        for i in range(2):
            ns = float(input(f"Digite o {i + 1}º numero: "))
            conta.append(ns)
        sub = conta[0] - conta[1]
        print(f"{conta[0]} - {conta[1]} = {sub}")
        op = int(input("Escolha uma opção: "))


    elif op == 3:
        print("Opção de MULTIPLICAÇÃO selecionada")
        for i in range(2):
            ns = float(input(f"Digite o {i + 1}º numero: "))
            conta.append(ns)
        mult = conta[0] * conta[1]
        print(f"{conta[0]} * {conta[1]} = {mult}")
        op = int(input("Escolha uma opção: "))

    elif op == 4:
        print("Opção de DIVISÃO selecionada")
        for i in range(2):
            ns = float(input(f"Digite o {i + 1}º numero: "))
            conta.append(ns)
        if conta[1] == 0:
            print("Não é possivel dividir por 0")
            op = int(input("Escolha uma opção: "))
        else:
            div = conta[0] / conta[1]
            print(f"{conta[0]} / {conta[1]} = {div}")
            op = int(input("Escolha uma opção: "))
print("Calculadora encerrada")

