


from weapon import Weapon


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 5
        self.weapon = Weapon("Ray_Gun",1)


    def robot_attack(self, dinosaur):
        dinosaur.health -= self.weapon.power
        print(f'{dinosaur.name} is being attacked by {self.name} with a {self.weapon.name} for {self.weapon.power} damage, leaving {dinosaur.name} with {dinosaur.health} health reamining')

