# Crie um programa que leia a largura e a altura em metros de uma parede e calcule a sua área e a quantidade de tinta
# necessária para pintar essa parede, sabendo que um litro de tinta, pinta 2 metros quadrados de parede
la = float(input('Qual a largura da parede? '))
al = float(input("Qual a altura da parede? "))
print(f"A área dessa parede é de {la*al} metros quadrados. Serão necessários {(la*al) / 2} litro(s) de tinta para pintá-la ")
