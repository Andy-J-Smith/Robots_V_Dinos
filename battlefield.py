
from select import select
from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def run_game(self):

        self.game_over = False
        self.round = 0
        

    
    def display_welcome(self):
        print("******Welcome to Robots versus Dinosaurs******")
        print("Who will win? The HERD or The FLEET")
        print("Lets Get it On!")

    def battle(self):
        self.fleet.robot_list[0].robot_attack(self.herd.dinosaurs_list[1])
        self.herd.dinosaurs_list[0].dino_atk(self.fleet.robot_list[1])


    def dino_turn(self, dinosaur):
        self.herd.dinosaurs_list[1]
        self.herd.dinosaurs_list[0]
        self.herd.dinosaurs_list[2]

    def robot_turn(self, robot):
        self.fleet.robot_list[1]
        self.fleet.robot_list[0]
        self.fleet.robot_list[2]
        print(self.fleet.robot_list[1])

    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        pass


