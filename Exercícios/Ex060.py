num = int(input("Digite um número: "))
c = num
factorial = 1
print(f"{num}! = ", end='')
while c != 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    factorial *= c
    c -= 1
print(f"{factorial}", end='')