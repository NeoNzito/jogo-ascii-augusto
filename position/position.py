class Corner:
    def __init__(self, pos_x:int, pos_y:int):
        self.x = pos_x
        self.y = pos_y

class Position(Corner):
    def __init__(self, pos_x:int, pos_y:int, width:int = 0, height:int = 0):
        self.x = pos_x
        self.y = pos_y
        self.width = width
        self.height = height
        self.top_left = Corner(self.x, self.y)
        self.top_right = Corner(self.x + self.width, self.y)
        self.bottom_left = Corner(self.x, self.y + self.height)
        self.bottom_right = Corner(self.x + self.width, self.y + self.height)

        