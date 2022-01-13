# crie um programa que leia a idade de um homem, e diga as condições de alistamento ao exército
import datetime
AnoAtual = datetime.datetime.now()
Data = AnoAtual.date()
ano = int(Data.strftime('%Y'))
nascimento = int(input("Em qual ano você nasceu? "))
idade = ano - nascimento
if idade == 18:
    print("Está na hora de se alistar, jovem!")
elif idade < 18:
    print(f"Você ainda não está na idade de alistamento. Ainda faltam {18 - idade} ano(s)")
elif idade > 18:
    print(f"Você já passou da hora de se alistar. Está atrasado em {idade - 18} ano(s)!")