txt = str(input("Digite uma frase: ")).strip().lower()
real = txt.replace(" ", "")
inverted = txt[::-1].replace(" ", "")
print(f"A frase '{real}' invertida fica '{inverted}'")
if inverted == real:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo")

# Método do Guanabara: Usando FOR
#
# frase = str(input)
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) -1, -1, -1):
# inverso = junto +- letra
# if inverso == junto:
#   print("É um palíndromo")
# else:
#   print("Não é um palíndromo")
#