primeiro_termo = int(input("Qual o primeiro termo da PA? "))#lê o primeiro termo
razao = int(input("Qual é a razão da PA? "))#lê a razão
print("Os 10 primeiros termos dessa PA são: ")#escreve isso aí
cont = 1#um contador pra ver quantas vezes a razão foi adicionada ao primeiro termo
total = 0#total de termos a serem mostrados
mais = 10
while mais != 0:
    total = total + mais#os 10 termos iniciais
    while cont <= total:
        print(f"{primeiro_termo} -> ", end='')
        primeiro_termo += razao#aqui, o primeiro termo recebe a razão
        cont += 1#um contador para limitar a quantidade de termos
    print("PAUSA")
    mais = int(input("Quantos termos a mais você deseja mostrar? "))#após serem mostrados os 10 primeiros termos,
    #é perguntado se precisamos de mais. Se a resposta != 0, mais = número escrito, e vão ser mostrados tantos mais
    #termos dessa PA.
print(f"Progressão finalizada com {total} termos")