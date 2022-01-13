# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

from utilidadesCeV import moedas
from utilidadesCeV import dado

numero = dado.leia_dinheiro("Digite um valor: R$")

# print(f"A metade de {moedas.moeda(numero)} é: {moedas.metade(numero, formatar=True)}")
# print(f"O dobro de {moedas.moeda(numero)} é: {moedas.dobro(numero, formatar=True)}")
# print(f"Aumentando {moedas.moeda(numero)} em 10%, temos: {moedas.aumentar(numero, 10, formatar=True)}")
# print(f"Diminuindo {moedas.moeda(numero)} em 10%, temos: {moedas.reduzir(numero, 10, formatar=True)}")

moedas.resumo(numero, 15, 15)
