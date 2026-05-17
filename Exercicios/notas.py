nome = str(input("Digite seu nome: "))
nota = float(input("Digite sua nota: "))
if nota >= 7.0:
    print(f"{nome}, você foi aprovado!!")
elif nota >= 5.0 and nota < 7.0:
    print(f"{nome}, você está de recuperação!!")
else:    
    print(f"{nome}, você foi reprovado!!")