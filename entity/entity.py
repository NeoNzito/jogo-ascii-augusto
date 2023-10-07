import WConio2
from position.position import Position

class Entity:
    def __init__(self, position_x:int, position_y:int, width:int, height:int):
        self.position = Position(position_x, position_y, width, height)
        self.image = ""
        self.active = False

    def update(self):
        pos_y = self.position.y
        if self.active:
            for lines in self.image:
                WConio2.gotoxy(self.position.x, pos_y)
                print(lines)
                pos_y += 1
                if pos_y > self.position.height + self.position.y:
                    pos_y = self.position_y

    def in_collision_area(self, position:Position) -> bool:
            top_left_collision = (self.position.top_left.x <= position.top_left.x <= self.position.top_right.x) and (self.position.top_right.y <= position.top_right.y <= self.position.bottom_right.y)
            top_right_collision = (self.position.top_left.x <= position.top_right.x <= self.position.top_right.x) and (self.position.top_right.y <= position.top_right.y <= self.position.bottom_right.y)
            bottom_left_collision =  (self.position.bottom_left.x <= position.bottom_left.x <= self.position.bottom_right.x) and (self.position.top_right.y <= position.top_right.y <= self.position.bottom_right.y)
            bottom_right_collision = (self.position.bottom_left.x <= position.bottom_right.x <= self.position.bottom_right.x) and (self.position.top_right.y <= position.top_right.y <= self.position.bottom_right.y)
            return top_left_collision or top_right_collision or bottom_left_collision or bottom_right_collision

    def get_position(self) -> Position:
        return self.position

class EntityList:
    entity_list = []

    @classmethod
    def set_list(cls, entity_list):
        if all(isinstance(entity, Entity) for entity in entity_list):
            cls.entity_list = entity_list
        else:
            raise ValueError("The list must contain only Entity type or it subclasses")