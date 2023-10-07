from entity.entity import EntityList, Position

class Collision:
    @classmethod
    def handle_player_collision(self): #Player always the first index from the entity list
        player = EntityList.entity_list[0]
        player_position = player.get_position()
        
        dx, dy = 0, 0

        if player.facing_direction.RIGHT:
            dx = 1
        elif player.facing_direction.LEFT:
            dx = -1
        elif player.facing_direction.DOWN:
            dy = 1
        elif player.facing_direction.UP:
            dy = -1

        new_position = Position(player_position.x + dx, player_position.y + dy, player_position.width, player_position.height)
        for i in range(1, len(EntityList.entity_list)):
            entity = EntityList.entity_list[i]
            if entity.in_collision_area(new_position):
                    player.position = Position(player_position.x + (dx * -1), player_position.y + (dy * -1), player.position.width, player.position.height)
        return True