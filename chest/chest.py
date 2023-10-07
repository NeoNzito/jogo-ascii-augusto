from entity.entity import Entity

class Chest(Entity):
    IMAGE = ["_____",
             "| U |",
             "|___|"]
    
    def __init__(self, position_x:int, position_y:int):
        super().__init__(position_x, position_y, 5, 3)
        self.image = self.IMAGE
        self.active = True

    def update(self):
        super().update()