nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
print(f"Nome:{nome}")
print(f"idade: {idade}")
print(f"Peso: {peso}kg")
if idade < 16:
    print("Treino não permitido para menores de 16")
else:
    print(f"Cadastro realizado!")
