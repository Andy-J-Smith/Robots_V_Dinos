from robot import Robot




class Fleet:
    def __init__(self):
        self.robot_list = []
        self.create_fleet()



    def create_fleet(self):
        bot1 = Robot("Terminator")
        self.robot_list.append(bot1)
        bot2 = Robot("Lance_Bishop")
        self.robot_list.append(bot2)
        bot3 = Robot("Johnny_5")
        self.robot_list.append(bot3)
        
