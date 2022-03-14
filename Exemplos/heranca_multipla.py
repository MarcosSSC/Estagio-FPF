class Player:
    def kick(self):
        print('Eu sei chutar a bola')

class Swimmer:
    def swimm(self):
        print('Eu sei nadar')

class Person(Player, Swimmer):
    def __init__(self, name=None, weight=None):
        self.name = name
        self.weight = weight

p = Person()
p.name = 'Marcos'
p.weight = '90'
p.kick()
p.swimm()

print(p)