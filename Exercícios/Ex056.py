grupo_media = 0
mulheres_menos_de_20 = 0
nome_homem = ''
idade_homem = 0
quantidade = int(input("O grupo é de quantas pessoas? "))
for info in range(1, quantidade + 1):
    nome = str(input(f"Digite o nome da {info}ª pessoa: ")).strip().title()
    idade = int(input(f"Digite a idade da {info}ª pessoa: "))
    grupo_media += idade
    sexo = str(input(f"Digite o sexo da {info}ª pessoa, usando 'F' para feminino e 'M' para masculino: ")).strip().capitalize()
    if sexo == 'F' and idade < 20:
        mulheres_menos_de_20 += 1
    if info == 1 and sexo == 'M':
        idade_homem = idade
        nome_homem = nome
    if sade > iexo == 'M' and iddade_homem:
        idade_homem = idade
        nome_homem = nome
print(f"A média de idade do grupo é de {grupo_media / quantidade}")
print(f"Neste grupo, existe(em) {mulheres_menos_de_20} mulher(es) com menos de 20 anos de idade.")
print(f"O homem mais velho desse grupo se chama {nome_homem}, e ele tem {idade_homem} anos.")
