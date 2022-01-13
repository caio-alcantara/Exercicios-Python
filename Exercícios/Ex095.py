# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
gols_jogador = []
lista_jogadores = []
lista_gols = []
continuar = ''
parar = 0


while continuar != 'N':
    jogador['Nome'] = str(input("Digite um nome: "))
    partidas = int(input("Quantas partidas foram jogadas? "))

    for c in range(1, partidas + 1):
        gols_jogador.append(int(input(f"    Quantos gols {jogador['Nome']} fez na {c}ª partida? ")))
        jogador['Gols'] = gols_jogador[:]
        jogador['Total de gols'] = sum(gols_jogador)
    lista_gols.append(jogador['Gols'])

    continuar = str(input("Quer adicionar outro jogador? [S/N] ")).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Opção inválida. Quer adicionar outro jogador? [S/N] "))

    lista_jogadores.append(jogador.copy())
    jogador.clear()
    gols_jogador.clear()


print('-' * 60)
print(f"{'NO.':<4}", end='')
for i in lista_jogadores[0].keys():
    print(f"{i:<15}", end='')
print()
print('-' * 60)

for i, e in enumerate(lista_jogadores):
    print(f"{i:<4}", end='')
    for d in e.values():
        print(f"{str(d):<15}", end='')
    print()

print('-' * 60)
while parar != 999:
    parar = int(input("Mostrar dados de qual jogador? [999 p/ parar] "))
    while parar >= len(lista_jogadores) and parar != 999:
        parar = int(input("Opção inválida. Deseja mostrar as estatísticas de qual jogador? [999 p/ parar) "))
    if parar == 999:
        print("Terminando o programa.")
    else:
        print('-' * 30)
        print(f"As estatísticas do jogador {lista_jogadores[parar]['Nome']} são: ")
        print('-' * 30)
        for c in range(0, len(lista_jogadores[parar]['Gols'])):
            print(f"Na partida {c+1}, ele marcou {lista_jogadores[parar]['Gols'][c]} gol(s).")
        print('-' * 30)
