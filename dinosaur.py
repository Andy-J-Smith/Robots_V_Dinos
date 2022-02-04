




class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 5

    def dino_atk(self,robot):
        robot.health -= self.attack_power
        print("Robot loses 1 health")




