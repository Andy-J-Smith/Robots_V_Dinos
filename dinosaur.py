




class Dinosaur:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 5

    def dino_atk(self,robot):
        robot.health -= self.attack_power
        print(f'{robot.name} is being attacked by {self.name} for {self.attack_power} damage, leaving {robot.name} with {robot.health} health remaining')
        




