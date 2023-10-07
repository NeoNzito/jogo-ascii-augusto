from screen.screen import Screen
import os 

class ScreenManager:
    def start(self, initial_screen:Screen):
        self.screen = initial_screen
        self.screen.start()

    def change_screen(self, new_screen:Screen):
        self.screen.on_exit()
        self.screen = new_screen
        self.screen.start()
    
    def update_screen(self):
        self.screen.update()