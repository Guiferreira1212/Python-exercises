import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

alunos = []
MEDIA_APROVACAO = 7.0 
limpar_tela()
print("========== SISTEMA DE NOTAS ==========")


while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar o cadastro): ").strip()
    

    if nome.lower() == 'sair':
        break
    

    while True:
        nota_str = input(f"Digite a nota de {nome}: ").replace(',', '.') 
        
     
        if nota_str.replace('.', '', 1).isdigit():
            nota = float(nota_str)
            if 0 <= nota <= 10:
                break
            else:
                print("❌ A nota deve estar entre 0 e 10!")
        else:
            print("❌ Valor inválido! Digite apenas números.")
    
  
    alunos.append({
        "nome": nome,
        "nota": nota
    })
    print(f"✅ Aluno(a) {nome} cadastrado(a) com sucesso!\n")

limpar_tela()


if len(alunos) == 0:
    print("Nenhum aluno foi cadastrado.")
else:
    print("========== BOLETIM DA TURMA ==========")
    

    for aluno in alunos:
        status = "Aprovado(a)" if aluno["nota"] >= MEDIA_APROVACAO else "Reprovado(a)"
        print(f"{aluno['nome']} - {aluno['nota']:.1f} - {status}")
    
    print("\n========== ESTATÍSTICAS ==========")
    

    apenas_notas = [aluno["nota"] for aluno in alunos]
    
    media_turma = sum(apenas_notas) / len(alunos)
    maior_nota = max(apenas_notas)
    menor_nota = min(apenas_notas)
    
    print(f"Média da turma: {media_turma:.1f}")
    print(f"Maior nota: {maior_nota:.1f}")
    print(f"Menor nota: {menor_nota:.1f}")
