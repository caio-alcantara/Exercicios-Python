num = int(input("Digite um número: "))
divisible = 0
for c in range(1, num+1):
    if num % c == 0:
        print("\33[33m", end='')
        divisible += 1
    else:
        print("\33[31m", end='')
    print(c, end=' ')
if divisible > 2:
    print(f"\n\33[7mO número {num} pôde ser dividido {divisible} vezes e, portanto, não é primo.\33[m", end='')
elif divisible == 2:
    print(f"\n\33[7mO número {num} pôde ser dividido apenas 2 vezes e, portanto, é primo.\33[7m", end='')