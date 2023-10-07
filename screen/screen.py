import WConio2
import os
from settings.settings import Window

class Screen:
    def __init__(self, name:str, width:int, height:int, position_x:int = 0, position_y:int = 0, clear_on_enter:bool = False, active_on_enter:bool = True): # MAX_WIDTH: 260 MAX_HEIGHT: 29 IN VSCODE
        self.name = name
        self.width = min(width, Window.MAX_WIDTH)
        self.height = min(height, Window.MAX_HEIGHT)
        self.active = False
        self.position_x = position_x
        self.position_y = position_y
        self.clear_on_enter = clear_on_enter
        self.active_on_enter = active_on_enter


    def start(self):
        if self.clear_on_enter:
            os.system("cls")
        self.screen = [[" " for _ in range(self.width)] for _ in range(self.height)]

        for lines in range(self.height):
            for columns in range(self.width):
                if (lines == 0 or lines == self.height - 1) or (columns == 0 or columns == self.width - 1):
                    self.screen[lines][columns] = "*"

    def update(self):
        pos_y = self.position_y
        if self.active:
            for lines in self.screen:
                map = ""
                for columns in lines:
                    map += columns
                WConio2.gotoxy(self.position_x, pos_y)
                print(map)
                pos_y += 1
                if pos_y > self.height:
                    pos_y = self.position_y
                

    def on_exit(self):
        self.active = False
