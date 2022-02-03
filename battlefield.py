from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def run_game(self):
        self.display_welcome()

    
    def display_welcome(self):
        pass

    def battle(self):
        self.dino_turn()   #add conditionals into function
        self.robot_turn()

    def dino_turn(self, dinosaur):
        pass

    def robot_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        pass
    