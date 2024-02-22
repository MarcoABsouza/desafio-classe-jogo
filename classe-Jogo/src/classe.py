class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def attack(self):
        ataque = ""
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "atacou com força bruta"
        print(f"O {self.tipo} atacou usando {ataque}")


heroi1 = Heroi("Gandalf", 1000, "mago")
heroi1.attack()
