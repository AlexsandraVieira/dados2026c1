#Cria um algoritmo para dizer de uma pessoa é maior de idade ou não
# idade = int(input("Qual a sua idade? "))

# if idade >= 18:
#     print("Você é maior de idade")
#     print("Pode tirar carteira de motorista")
# else:
#     print("Você é menor de idade")
#     faltam = 18 - idade
#     print(f"Faltam {faltam} anos para completar 18.")

# print("Fim do Programa")
# Faça um algoritmo para dizer se o número é par ou ímpar

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    paridade = "par"
else:
    paridade = "impar"

print(f"{numero} é {paridade}")    
