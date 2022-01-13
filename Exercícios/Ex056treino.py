nome_mulher = ''
idade_mulher = 0
for info in range(1, 5):
    nome = str(input(f"Digite {info}º nome: ")).strip().capitalize()
    sexo = str(input(f"Digite o {info}º sexo: ")).strip().capitalize()
    idade = int(input(f"Digite a {info}ª idade: "))
    if info == 1 and sexo == 'F':
        nome_mulher = nome
        idade_mulher = idade
    if sexo == 'F' and idade > idade_mulher:
        nome_mulher = nome
        idade_mulher = idade
print(f"A mulher mais velha desse grupo tem {idade_mulher} anos e se chama {nome_mulher}.")
