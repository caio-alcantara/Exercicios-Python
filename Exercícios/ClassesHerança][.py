class Animal:
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor

    def descricao(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos de idade e sou de cor {self.cor}.")


class Gato(Animal):
    def miar(self):
        print("miau")


class Cachorro(Animal):
    def latir(self):
        print("au")


class Macaco(Animal):
    def falar(self):
        print("uh-uh ah-ah")


Tino = Cachorro("Tino", 8, "Branco")
Tino.descricao()
Tino.latir()
Jaime = Gato("Jaime", 3, "Preto")
Jaime.descricao()
Jaime.miar()
Lucas = Macaco("Lucas", 15, "Preto")
Lucas.descricao()
Lucas.falar()