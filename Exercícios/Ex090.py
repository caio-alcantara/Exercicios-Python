# Faça um programa que leia nome e média de um aluno,
# guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno_dic = {}

aluno_dic['Nome'] = str(input("Digite o nome: "))
aluno_dic['Média'] = float(input(f"Digite a média de {aluno_dic['Nome']}: "))

if aluno_dic['Média'] >= 7:
    aluno_dic['Situação'] = 'Aprovado'
elif 6 <= aluno_dic['Média'] < 7:
    aluno_dic['Situação'] = 'Recuperação'
elif aluno_dic['Média'] < 6:
    aluno_dic['Situação'] = 'Reprovado'

print('-=' * 10)

for key, value in aluno_dic.items():
    print(f"O campo {key} é: {value}.")