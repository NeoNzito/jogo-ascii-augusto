from screen.screen import Screen, os

class MapScreen(Screen):
    def __init__(self, name:str, width:int, height:int, position_x:int = 0, position_y:int = 0):
        super().__init__(name, width, height, position_x, position_y, True)

    def start(self):
        super().start()
        self.active = True
    
    def update(self):
        super().update()
    
    def on_exit(self):
        super().on_exit()
        os.system("cls")