from dinosaur import Dinosaur




class Herd:
    def __init__(self):
        self.dinosaurs_list = []
        self.create_herd()
        

    def create_herd(self):
        dino1 = Dinosaur("T-Rex",1)
        self.dinosaurs_list.append(dino1)
        dino2 = Dinosaur("Raptor",1)
        self.dinosaurs_list.append(dino2)
        dino3 = Dinosaur("Bronto",1)
        self.dinosaurs_list.append(dino3)
        
        

        



