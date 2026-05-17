import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:

    print("\n=== Menu ===")
    print("1 - Hamburguer = R$20,00 \n")
    print("2 - Batata = R$10,00 \n")
    print("3 - Refrigerante = R$8,00")

    opcao = input("\nSelecione a opção desejada: ")
    quantidade = int(input("Selecione a quantidade desejada: "))
    limpar_tela()
    if opcao == "1":
        print(f"Você escolheu {quantidade} hamburguer")
        produto = "Hamburguer"
        valor = quantidade * 20
    elif opcao == "2":
        print(f"Você escolheu {quantidade} batata ")
        produto = "Batata"
        valor = quantidade * 10
    elif opcao == "3":
        print(f"Você escolheu {quantidade}  refrigerante")
        produto = "Refrigerante"
        valor = quantidade * 8
    else:
        print("Opção inválida!")
        continue
    limpar_tela()
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Total: R${valor}")

    mais = input("Deseja algo a mais? (s/n): ")
    if mais.lower() == "n":
        print("Obrigado pela compra")
        break
