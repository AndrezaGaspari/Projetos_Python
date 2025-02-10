
import os

while True:
    print("Calculadora")
    print("============")
    print("0: SOMA")
    print("1: SUBTRAÇÃO")
    print("2: MULTIPLICAÇÃO")
    print("3: DIVISAO")
    print("4: EXPONENCIAÇÃO")
    print("5: Encerrando calculadora")

    try:
        opcao = int(input("Escolha a Operação que deseja realizar:  "))

        if opcao == 5:
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in range(6):
            print("Erro: Opção inválida. Tente novamente.")
            continue

    # Limpar tela antes de pedir os números
        os.system('cls' if os.name == 'nt' else 'clear')

        n1= float(input("Digite o primeiro número:  "))
        n2= float(input("Digite o segundo número:  "))

    # Limpar tela antes de pedir os números
        os.system('cls' if os.name == 'nt' else 'clear')

        if opcao == 0:
            soma = n1+n2
            print("A soma é:{}".format(soma))
        elif opcao == 1:
            sub= n1-n2
            print("A subtração é:{}".format(sub))
        elif opcao == 2:
            multi= n1*n2
            print("A multiplicação é:{}".format(multi))
        elif opcao == 3:
            divi= n1/n2
            print("A divisão é:{}".format(divi))
        elif opcao ==4:
            exp= n1**n2
            print("A exponenciação é:{}".format(exp))
        else:
            print("A opção desejada não existe!!!")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")






