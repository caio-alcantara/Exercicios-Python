# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista = []
dic = {}
continuar = ''
idades = 0
lista_mulheres = []

while continuar != 'N':
    dic.clear()
    dic['Nome'] = str(input("Digite um nome: "))
    dic['Idade'] = int(input("Digite uma idade: "))
    idades += dic['Idade']

    dic['Sexo'] = str(input("Digite um sexo: [F/M} ")).strip().upper()
    while dic['Sexo'] != 'F' and dic['Sexo'] != 'M':
        dic['Sexo'] = str(input("Digite um sexo: [F/M} ")).strip().upper()

    if dic['Sexo'] == 'F':
        lista_mulheres.append(dic['Nome'])

    lista.append(dic.copy())

    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()

print(f"A) Ao todo, temos {len(lista)} pessoas cadastradas.")

print(f"B) A média de idade das pessoas cadastradas é de: {idades / len(lista)} anos.")

if len(lista_mulheres) != 0:
    print(f"C) A lista de mulheres é composta por: {lista_mulheres}")
else:
    print("Não foram cadastradas mulheres.")

print("D) Lista de pessoas acima da média:", end='')
for p in lista:
    if p['Idade'] > (idades / len(lista)):
        print('    ')
        for key, value in p.items():
            print(f"{key}: {value}; ", end='')
        print()

print("___ PROGRAMA ENCERRADO ___")