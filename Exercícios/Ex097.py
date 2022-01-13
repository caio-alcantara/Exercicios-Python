# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(text):
    print('=' * (len(text) + 1))
    print(text)
    print('=' * (len(text) + 1))


# Programa principal
texto = str(input("Digite um texto: ")).strip()
escreva(texto)
