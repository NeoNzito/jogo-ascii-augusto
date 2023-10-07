from entity.entity import Entity
from position.position import Position

class LiveEntity(Entity):
    def __init__(self, position_x: int, position_y: int, width: int, height: int, health:float):
        super().__init__(position_x, position_y, width, height)
        self.health = health
        
    def update(self):
        return super().update()
    
    def in_collision_area(self, position: Position) -> bool:
        return super().in_collision_area(position)
    
    def get_position(self) -> Position:
        return super().get_position()
    
    def damage(self, damage:float):
        self.health -= damage