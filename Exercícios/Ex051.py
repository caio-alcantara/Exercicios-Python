first = int(input("Qual o primeiro termo da Progressão Aritmética? "))
razao = int(input("Qual a razão dessa Progressão Aritmética? "))
a = int(input("Quantos termos termos dessa PA você quer ver? "))
print(f"\33[7mOs {a} primeiros termos dessa PA são:\33[m")
for n in range(1, a + 1):
    print(f"\33[31mO {n}º termo dessa PA é: {first + (n - 1) * razao}.\33")

