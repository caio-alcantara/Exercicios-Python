nota1 = float(input("Qual foi a primeira nota? "))
nota2 = float(input("Qual foi a segunda nota? "))
media = (nota1 + nota2) / 2
print(f"A sua média foi de {media} ponto(s). Com essa nota:")
if media >= 7.0:
    print("Parabéns! Você já está aprovado.")
elif 5.0 <= media <= 6.9:
    print("Você irá precisar fazer uma prova de recuperação. Boa sorte!")
elif media < 5.0:
    print("Você foi reprovado!")
