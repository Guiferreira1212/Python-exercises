produto = str(input("Qual produto desejado?: "))
preço = float(input("Qual o preço do produto?: "))
quantidade = int(input("Qual a quantidade do produto?: "))
preço_total = preço * quantidade
print(f"O preço total do produto é: {preço_total}")

if preço_total > 100:
    print("Você ganhou 10% de desconto!")
    desconto = preço_total * 0.10
    preço_com_desconto = preço_total - desconto
    print(f"O preço com desconto é: {preço_com_desconto}")
else:
    print("Você não ganhou desconto.") 