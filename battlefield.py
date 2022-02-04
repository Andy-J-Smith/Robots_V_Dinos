
from select import select
from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def run_game(self):
        self.display_welcome()
        self.robot_turn()
        pass
        

    
    def display_welcome(self):
        print("******Welcome to Robots versus Dinosaurs******")
        print("Who will win? The HERD or The FLEET")
        print("Lets Get it On!")

    def battle(self):
        
            
        self.herd.dinosaurs_list[0].dino_atk(self.fleet.robot_list[1])


    def dino_turn(self):
        self.herd.dinosaurs_list[1].health -= 1
       

    def robot_turn(self):
        print("select a robot to attack with")
        self.show_robot_options()
        user_robot_choice = int(input())
        self.fleet.robot_list[user_robot_choice].robot_attack(self.herd.dinosaurs_list[1])
        pass

    def show_dino_options(self):
        pass

    def show_robot_options(self):
        count = 0
        for robot in self.fleet.robot_list:
            print(f'Press {count} to select {robot.name}')
            count += 1
        pass

    def display_winners(self):
        pass




