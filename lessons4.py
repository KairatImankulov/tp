class Elf():
    number_of_eyes = 2
    numder_of_hands = 2
    numder_of_legs = 2
    hair_color = "black"
    name = "Rolli"
    bow_type = "wood"
    tribe = "Minyar"
    number_of_arows = 10
    boss = "Big boss"
    rang = 1

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return 'Здраствуйте господин'

    def improve(self):
        self.rang += 1
        if self.rang >= 5:
            return 'sniper'
        else:
            return self.rang 

    def decrease(self):
        self.number_of_arows -= 1
        return self.number_of_arows

warrior = Elf("Rolly")
print(warrior.greeting())
print(warrior.improve())
print(warrior.decrease())
print(warrior.improve())
print(warrior.decrease())
print(warrior.improve())
print(warrior.improve())
print(warrior.improve())

class Magician():
    number_of_eyes = 2
    numder_of_hands = 2
    numder_of_legs = 2
    hair_color = "white"
    name = "Satoru"
    detachment = "Godjo"
    element = "fire"
    weapons = "staff"
    number_of_mana = 10
    boss = "boss"
    rang = 1

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return 'здраствуй господин'
    
    def improve(self):
        self.rang += 1
        if self.rang >= 5:
            return 'archimag'
        else:
            return self.rang
        
    def decrease(self):
        self.number_of_mana -= 1
        return self.number_of_mana
    
warrior = Magician("Satoru")
print(warrior.greeting())
print(warrior.improve())
print(warrior.decrease())
print(warrior.improve())
print(warrior.decrease())
print(warrior.improve())
print(warrior.improve())
print(warrior.improve())

