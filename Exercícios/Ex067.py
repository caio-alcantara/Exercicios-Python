from time import sleep
while True:
    num = int(input("De qual valor você quer saber a tabuada? [Digite um valor negativo para parar] "))
    if num < 0:
        break
    for c in range(1, 11):
        print(f"{num} x {c} = {num * c}")
print("\33[7mENCERRANDO O PROGRAMA...\33[m")
sleep(1)
print("\33[7mPROGRAMA ENCERRADO. VOLTE SEMPRE!\33[m")