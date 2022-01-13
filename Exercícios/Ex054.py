from datetime import date
ano = int(date.today().year)
maior_de_idade = 0
menor_de_idade = 0
pessoas = int(input("Qual a quantidade de pessoas que você quer saber se são maiores ou não? "))
for n in range(1, pessoas + 1):
    nascimento = int(input(f"Qual o ano de nascimento da {n}ª pessoa? "))
    idade = ano - nascimento
    if idade < 18:
        menor_de_idade += 1
    else:
        maior_de_idade += 1
print(f"Dessas {pessoas} pessoas, {maior_de_idade} são maiores de idade, e {menor_de_idade} são menores de idade.")
