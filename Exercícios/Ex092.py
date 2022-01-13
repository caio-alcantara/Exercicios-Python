# Crie um programa que leia nome,
# ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
ano_atual = int(date.today().year)

trabalhador = {}

trabalhador['Nome'] = str(input("Digite o nome do(a) trabalhador(a): "))
Nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - Nascimento
trabalhador['Idade'] = idade
trabalhador['CTPS'] = int(input("Carteira de Trabalho: (0 caso não possua) "))

if trabalhador['CTPS'] != 0:
    trabalhador['Ano de contratação'] = int(input("Ano de contratação: "))
    ano_aposentadoria = (trabalhador['Ano de contratação'] + 35) - Nascimento
    trabalhador['Aposentadoria'] = ano_aposentadoria
    trabalhador['Salário'] = float(input("Salário: [R$] "))

for key, valor in trabalhador.items():
    print(f"{key}: {valor}.")
    