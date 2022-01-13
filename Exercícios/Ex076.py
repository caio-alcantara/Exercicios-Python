# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tup = ('Lápis', '2.00', 'Borracha', '0.75', 'Esquadros', '80.00', 'Mochila', '200.00', 'Pasta', '8.00')
print('=' * 50)
print(f"{'LISTA DE PREÇOS:':^50}")
print('=' * 50)
for pos in range(len(tup)):
    if pos % 2 == 0:
        print(f'{tup[pos]:.<30}', end='')
    else:
        print(f'R${tup[pos]:>4}')
print('=' * 50)