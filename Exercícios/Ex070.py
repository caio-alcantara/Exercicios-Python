total_gasto = mais_de_mil = menor_preco = contador = 0
continuar = ' '
mais_barato = ''
while True:
    produto = str(input("Qual é o nome do produto? ")).strip().capitalize()
    preco = float(input("Qual é o preço do produto? "))
    contador += 1
    continuar = ' '
    total_gasto += preco
    if preco > 1000:
        mais_de_mil += 1
    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        mais_barato = produto
    while continuar != 'S' and continuar != 'N':
        continuar = str(input("Quer adicionar mais produtos? [S/N] ")).strip().capitalize()[0]
    if continuar == 'N':
        break
print(f"O total da compra foi de R${total_gasto:.2f}.")
print(f"Foram comprados {mais_de_mil} produtos que custam mais de R$1000,00.")
print(f"O menor produto comprado foi o(a) {mais_barato}, e custou R${menor_preco:.2f}.")