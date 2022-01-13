maiores = homens = mulheres_menos = 0
continuar = ' '
while True:
    idade = int(input("Qual é a idade dessa pessoa? "))
    sexo = ' '
    continuar = ' '
    while sexo != 'M' and sexo != 'F':
        sexo = str(input("Qual é o sexo dessa pessoa? [F/M] ")).strip().capitalize()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos += 1
    while continuar != 'N' and continuar != 'S':
        continuar = str(input("Deseja inserir dados de outra pessoa? [S/N] ")).strip().capitalize()[0]
    if continuar == 'N':
        break
print(f"De todas essas pessoas, {homens} é(são) homem(s), {maiores} tem mais de 18 anos e {mulheres_menos} é(são) mulher(es) com menos de 20 anos.")