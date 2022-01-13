tup = ('Arroz', 'Feijao', 'Batata', 'Carne', 'Frango', 'Queijo', 'Amora')
for palavras in tup:
    print(f"\nNa palavra {palavras}, temos: ", end='')
    for letra in palavras:
        if letra in 'AEIOUaeiou':
            print(letra, end=' ')