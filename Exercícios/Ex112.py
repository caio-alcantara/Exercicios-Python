# Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja monetários.

# Ver no EX107, e no próprio pacote dados

from utilidadesCeV import dado

n = dado.leia_dinheiro("Digite um valor: ")
print(n)
