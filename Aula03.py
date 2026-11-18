#Cria um algoritmo para dizer de uma pessoa é maior de idade ou não
idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você é maior de idade")
    print("Pode tirar carteira de motorista")
else:
    print("Você é menor de idade")
    faltam = 18 - idade
    print(f"Faltam {faltam} anos para completar 18.")

print("Fim do Programa")
