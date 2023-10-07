from entity.live_entity import LiveEntity
from collision.collision import Collision
from direction.direction import Direction

class Character(LiveEntity):
    FRONT = [" O ",
             "/T\\",
             " ∧ "]

    BACK = [" O ",
            "/M\\",
            " ∧ "]

    RIGHT = [" O ",
            " L ",
            " | "]
            
    LEFT = [" O ",
            " ⅃ ",
            " | "]
    
    def __init__(self, position_x:int = 0, position_y:int = 0):
        super().__init__(position_x, position_y, 3, 3, 30)
        self.facing_direction = Direction.RIGHT
        self.image = self.FRONT
        self.active = True

    def handle_keys(self, keys:str):
        if (keys.lower() == "d"):
            self.facing_direction = Direction.RIGHT
            self.image = self.RIGHT
            if Collision.handle_player_collision():
                self.position.x += 1
        elif (keys.lower() == "a"):
            self.facing_direction = Direction.LEFT
            self.image = self.LEFT
            if Collision.handle_player_collision():
                self.position.x -= 1
        if (keys.lower() == "w"):
            self.facing_direction = Direction.UP
            self.image = self.BACK
            if Collision.handle_player_collision():
                self.position.y -= 1
        elif (keys.lower() == "s"):
            self.facing_direction = Direction.DOWN
            self.image = self.FRONT
            if Collision.handle_player_collision():
                self.position.y += 1

    def update(self):
        super().update()