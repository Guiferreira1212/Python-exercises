import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

password_fix = str(input("Defina a sua senha: "))

limpar_tela()
password = str(input("Digite sua senha: "))

while password != password_fix:
    print("\nSenha incorreta, tente novamente. ")
    password = str(input("Digite sua senha: "))

limpar_tela()
print("Acesso concedido! Bem-vindo.")
