# adding logic to dino options just like we did robot options DONE
# add a print to robot_turn() that says "choose a dino to attack" DONE
# then call show_dino_options  DONE
# add an input DONE
# replace the 1 in the index of the dino being passed in with the variable seupt for the input DONE
# now a user can pick the robot and the dino being attack! TEST IT-----TURNS TESTED GOOD.
# then you can do the same for dino turn
# think about wehre its goin to make sense to check and see if an oppend health dropped to 0 and remove them from the list
# test code update to repo
from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()
        pass
        

    
    def display_welcome(self):
        print("******Welcome to Robots versus Dinosaurs******")
        print("Who will win? The HERD or The FLEET")
        print("Lets Get it On!")

    def battle(self):
        length = len(self.fleet.robot_list)
        i = 0
        while i < length:
            self.robot_turn()
            i += 1
               
            continue                   # ONLY loops through list 1 time for a total of six turns. 
                                                # iterates 3 times for robot then 3 times for dino
        length = len(self.herd.dinosaurs_list)
        j = 0
        while j < length:
            self.dino_turn()
            j += 1
        
            continue
        
    def dino_turn(self):
        print ("Select a dinosaur to attack with ")
        self.show_dino_options()
        user_dino_choice = int(input())
        self.herd.dinosaurs_list[user_dino_choice].dino_atk(self.fleet.robot_list[1])
        # if self.fleet.robot_list.health() <= 0:                               
        #    self.fleet.robot_list.remove(self.fleet.robot_list)
        pass
                                                                                    # Had  to omit the remove functions. could not make them work.
    def robot_turn(self):
        print("select a robot to attack with ")
        self.show_robot_options()
        user_robot_choice = int(input())
        self.fleet.robot_list[user_robot_choice].robot_attack(self.herd.dinosaurs_list[1])
        # if self.herd.dinosaurs_list.health() <= 0:
        #    self.herd.dinosaurs_list.remove(self.herd.dinosaurs_list)
        pass

    def show_dino_options(self):
        count = 0
        for dino in self.herd.dinosaurs_list:
            print(f'Press {count} to select {dino.name}')
            count += 1
        

    def show_robot_options(self):
        count = 0
        for robot in self.fleet.robot_list:
            print(f'Press {count} to select {robot.name}')
            count += 1
        pass

    def display_winners(self):
        if self.fleet.robot_list() <= 0:
            print("Congratulations to The Dinosaurs")
        else:
            print("Congratulations to The Robots")
            
        pass




