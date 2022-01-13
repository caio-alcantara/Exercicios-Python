

from time import sleep


def linha():
    print('=' * 30)


def contagem(inicio, fim, passo):
    """
    Contador que irá analisar os parâmetros dados e mostrar na tela
    uma contagem que segue esses parâmetros.

    :param inicio: De qual valor a contagem irá ser iniciada
    :param fim: Onde a contagem irá parar
    :param passo: Qual o "rítmo" da contagem, ou "de quantas em quantas casas" o contador irá pular.
    :return: None
    """
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo += 1
    linha()
    print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}")
    linha()
    if inicio < fim:
        contador = inicio
        while contador <= fim:
            print(f"{contador}", end=' ')
            sleep(0.25)
            contador += passo
        print("FIM!")
    else:
        contador = inicio
        while contador >= fim:
            print(f"{contador}", end=' ')
            sleep(0.25)
            contador -= passo
        print("FIM!")


contagem(0, 10, 1)
print()
contagem(10, 0, 2)
print()
linha()
print("\33[7mPersonalize a contagem: \33[m")
linha()
i = int(input("De onde começar: "))
f = int(input("Onde parar: "))
p = int(input("Qual o passo: "))
contagem(i, f, p)
help(contagem)

