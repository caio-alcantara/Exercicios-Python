# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

numeros = []


def sorteia():
    from random import randint
    print('-' * 60)
    print("Sorteando os 5 valores para a lista: ")
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(f"Os valores sorteados foram: {numeros}")


def soma_par(lista):
    print('-' * 60)
    soma = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f"A soma dos valores pares de {lista} é: {soma}")


# Programa principal
sorteia()
soma_par(numeros)
