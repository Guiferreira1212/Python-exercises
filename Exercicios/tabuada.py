num1 = int(input("Digite um número para a tabuada: "))
print(f"Tabuada do {num1}:")
for i in range(1, 11):
    resultado = num1 * i
    print(f"{num1} x {i} = {resultado}")