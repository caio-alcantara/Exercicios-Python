from numpy import count_nonzero
a = int(input("De qual valor você quer começar? "))
b = int(input("Em qual valor você quer terminar? "))
s = [c for c in range(a, b+1, 2) if c % 3 == 0]
print(f"Existem {count_nonzero(s)} números ímpares e múltiplos de 3 nessa sequência. A soma deles é {sum(s)}")

# outro jeito de fazer seria:

# sum = 0
# for c in range(1, 501, 2):
#     if c % 3 == 0:
#        sum = sum + c
# print(f"A soma de todos os ímpares múltiplos de 3 entre 1 e 500 vale {soma}.")
