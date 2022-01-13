# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
continuar = ''
lista = []
dados = []
quantidade = 0

while continuar != 'N':
    nome = str(input("Nome: "))
    dados.append(nome)
    nota1 = float(input("Nota 1: "))
    dados.append(nota1)
    nota2 = float(input("Nota 2: "))
    dados.append(nota2)
    lista.append(dados[:])
    dados.clear()
    quantidade += 1
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Opção inválida. Deseja continuar? [S/N] ")).strip().upper()

print('-=' * 15)
print(f"{'NO.':<4}{'NOME':<10}{'MÉDIA:':>8}")
print('-' * 30)

for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<10}{(a[1] + a[2]) / 2:>8}")

print('-' * 30)

parar = 0
while parar != 999:
    parar = int(input("Mostrar notas de qual aluno? [999 p/ parar] "))
    while parar >= len(lista) and parar != 999:
        parar = int(input("Opção inválida. Deseja mostrar as notas de qual aluno? [999 p/ parar) "))
    if parar == 999:
        print("Terminando o programa.")
    else:
        print(f"As notas do aluno {lista[parar][0]} foram {lista[parar][1]} e {lista[parar][2]}.")
