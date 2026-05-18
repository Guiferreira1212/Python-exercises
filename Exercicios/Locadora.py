import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

quant_filmes = int(input("Quantos filmes?: "))
x = []
limpar_tela()

for i in range(quant_filmes):

    while True:
        print(f"=== Cadastrando o {i + 1}º filme ===")
        filme = input("Digite o filme: ")
        ano =  int(input("Digite o ano: "))

        dados_do_filme = {"titulo": filme, "ano": ano}
        
        if ano > 1900:
            x.append(dados_do_filme)
            limpar_tela()
            break
        else:
            print("Ano invalido! Digite os dados dos filmes novamente.")
            input("Pressione Enter para tentar novamente")
            limpar_tela()
print("=== Todos os filmes cadastrados ===")
for item in x:
    print(f"{item['titulo']} - {item['ano']}")
