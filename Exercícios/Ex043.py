# Crie uma calculadora de IMC
peso = float(input("Qual o seu peso em quilogramas? "))
altura = float(input("Qual a sua altura em metros? "))
imc = peso / altura**2
print(f"O seu IMC é de {imc:.2f}.")
if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif 18.5 <= imc < 25:
    print("Você está no seu peso ideal.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
elif 30 <= imc < 40:
    print("Você está com obesidade.")
elif imc > 40:
    print("Você está com obesidade \33[7mmórbida.\33[m")