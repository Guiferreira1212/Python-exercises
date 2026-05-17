import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


cliente = str(input("Digite seu nome: "))
valor_compra = float(input("Digite o valor da compra: "))
limpar_tela()

print(f"Nome: {cliente}")
print(f"Valor original: {valor_compra}")
if valor_compra >= 200:
    desconto = 20
    print("Compra com desconto de 20%")

elif valor_compra >= 100:
    desconto = 10
    print("Compra com desconto de 10%")

else:
    desconto = 0

valor_desconto = valor_compra * (desconto / 100)
valor_final = valor_compra - valor_desconto
print(f"Desconto aplicado: {desconto}%")
print(f"Valor final: R${valor_final}")
print(valor_final)


