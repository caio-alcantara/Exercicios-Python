primeiro_termo = int(input("Qual o primeiro termo dessa PA? "))
razao = int(input("Qual é a razão dessa PA? "))
print("\33[7mOs 10 primeiros termos dessa PA são:\33[m")
contador = 1
total_de_termos = 0
mais = 10
while mais != 0:
    total_de_termos = total_de_termos + mais
    while contador <= total_de_termos:
        print(f"{primeiro_termo} -> ", end='')
        primeiro_termo += razao
        contador += 1
    print("Pausa")
    mais = int(input("Quantos termos a mais você quer mostrar? "))
print(f"Fim da PA. Foram mostrados {total_de_termos} termos.")