import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

usuarios_cadastrados = {}

limpar_tela()
print("========== TELA DE CADASTRO ==========")
novo_usuario = input("Crie um nome de usuário: ").strip()
nova_senha = input("Crie uma senha: ").strip()


usuarios_cadastrados[novo_usuario] = nova_senha

print("\nCadastro realizado com sucesso!")
input("Pressione ENTER para ir para a tela de login...")



limpar_tela()
print("========== TELA DE LOGIN ==========")

tentativas_restantes = 3
login_sucesso = False


while tentativas_restantes > 0:
    print(f"Tentativas restantes: {tentativas_restantes}\n")
    usuario_login = input("Usuário: ").strip()
    senha_login = input("Senha: ").strip()

    if usuario_login in usuarios_cadastrados and usuarios_cadastrados[usuario_login] == senha_login:
        login_sucesso = True
        break 
    else:
        tentativas_restantes -= 1 
        limpar_tela()
        print("❌ Usuário ou senha incorretos!\n")


limpar_tela()
if login_sucesso:
    print("=====================================")
    print("✨ Login realizado com sucesso! ✨")
    print("=====================================")
else:
    print("=====================================")
    print("🔒 Acesso bloqueado! Excedeu 3 tentativas.")
    print("=====================================")
