#aqui eu fiz esses prints
#para ser o "manual" da calculadora 1.0

print("==============")
print("CALCULADORA")
print("==============")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair") 

#aqui começa minhas estrutura
#primeiro input para opção de conta
op = int(input("Escolha uma opção: "))

#usei while para fazer a repetição com a condição de que
#se a opção de saida "5" for operada, o codigo pare de repetir
while op != 5:
#minha variavel de lista, para armazenar os inputs recebidos
    conta =[]
# aqui as condições para que funcione cada uma das opções
    if op >= 6 or op <= 0:
        print("Escolha uma das opçoes existentes")
        op = int(input("Escolha uma opção: "))

    elif op == 1:
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
#mensagem de encerramento da calculadora 1.0 caso "5" seja a opçao desejada
print("Calculadora encerrada")