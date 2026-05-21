import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

tarefas = []

limpar_tela()

while True:
    print("\n========== TO-DO LIST ==========")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")
    print("================================")
    
    opcao = input("Escolha uma opção: ").strip()
    limpar_tela()
    
    if opcao == '1':
       
        nova_tarefa = input("Digite a nova tarefa: ").strip()
        tarefas.append(nova_tarefa)
        print(f"✅ Tarefa '{nova_tarefa}' adicionada com sucesso!")
        
    elif opcao == '2':
      
        print("--- Suas Tarefas ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
   
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa}")
                
    elif opcao == '3':
      
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
        else:
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa}")
            
            print("--------------------")
            
            numero_remover = input("Digite o NÚMERO da tarefa que deseja remover: ").strip()
            
            if numero_remover.isdigit():
                indice = int(numero_remover) - 1 
                
               
                if 0 <= indice < len(tarefas):
                    tarefa_removida = tarefas.pop(indice)
                    print(f"🗑️ Tarefa '{tarefa_removida}' removida com sucesso!")
                else:
                    print("❌ Tarefa não encontrada")
            else:
                print("❌ Por favor, digite um número válido.")
                
    elif opcao == '4':
        print("Saindo do programa... Até logo! 👋")
        break
        
    else:
        print("❌ Opção inválida! Tente novamente.")
