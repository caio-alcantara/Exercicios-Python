# Crie um programa que leia a idade de um nadador(a), e diga em que categoria ele(a) está
import datetime
AnoAtual = datetime.datetime.now()
Data = AnoAtual.date()
ano = int(Data.strftime('%Y'))
nascimento = int(input("Em qual ano o(a) nadador(a) nasceu? "))
idade = ano - nascimento
if idade <= 9:
    print("Este(a) nadador(a) está na cateforia MIRIM.")
elif 9 < idade <= 14:
    print("Este(a) nadador(a) está na categoria INFANTIL.")
elif 14 < idade <= 19:
    print("Este(a) nadador(a) está na categoria JUNIOR..")
elif 19 < idade <= 25:
    print("Este(a) nadador(a) está na categoria SÊNIOR.")
elif idade > 25:
    print("Este(a) nadador(a) está na categoria MASTER.")
