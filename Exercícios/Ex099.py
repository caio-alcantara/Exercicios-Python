# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# O seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def linha():
    print('=' * 45)


def maior(*num):
    linha()
    print(f"Analisando os valores passados...")
    print(f"Foram informados {len(num)} valores ao todo")
    if len(num) > 0:
        print(f"O maior valor foi {max(num)}")


#Programa principal
maior()
maior(1, 5)
maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior(4, 6, 1, 56, 1, 76, 1, 99)
maior()
maior(0)
