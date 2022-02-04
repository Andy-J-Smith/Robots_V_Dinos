from weapon import Weapon


class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 5
        self.weapon = Weapon("Ray_Gun",1)


    def robot_attack(self, dinosaur):
        dinosaur.health -= self.weapon
        print("Dinosaur loses 1 health")

