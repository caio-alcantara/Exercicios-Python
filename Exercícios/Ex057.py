n = ''
while n != 'F' and n != 'M':
    n = str(input("Digite um sexo [F/M]: ")).strip().capitalize()[0]
    if n != 'F' and n != 'M':
        print("Parece que você não digitou uma opção válida. Digite novamente.")
if n == 'M':
    print("O sexo digitado é masculino.")
elif n == 'F':
    print("O sexo digitado é feminino")
