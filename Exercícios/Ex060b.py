num = int(input("Digite um número: "))
c = num
factorial = 1
print(f"{num}! = ", end='')
for c in range(1, num+1):
    print(c, end='')
    print(' x ' if c < num else ' = ', end='')
    factorial *= c
print(factorial)
