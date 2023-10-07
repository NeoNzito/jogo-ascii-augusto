from screen.screen import Screen, os

class SideMenu(Screen):
    def __init__(self, name:str, width:int, height:int, position_x:int, position_y:int):
        super().__init__(name, width, height, position_x, position_y, True, False)

    def start(self):
        super().start()
    
    def update(self):
        super().update()
    
    def on_exit(self):
        super().on_exit()
        os.system("cls")