import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

quant_alu = int(input("Quantos alunos serão cadastrados?: "))
alunos = []
limpar_tela()

for i in range (quant_alu):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
limpar_tela()
print("Lista:")
for nome in alunos:
    print(nome)
