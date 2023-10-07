from settings.settings import Window
from screen.screen import Screen, WConio2
from screen.screen_manager import ScreenManager
from screen.side_menu_screen import SideMenu
from screen.map_screen import MapScreen
from character.character import Character
from chest.chest import Chest
from entity.entity import EntityList

class MainScreen(Screen):
    
    map_screen = MapScreen("map_screen", 110, 25)
    side_menu_screen = SideMenu("side_menu", 30, 25, 131, 0)
    manager = ScreenManager()
    screens = [side_menu_screen, map_screen]
    character = Character(50, 15)
    chest = Chest(75, 6)
    EntityList.set_list([character, chest])
    

    def __init__(self):
        super().__init__("Main Screen", Window.MAX_WIDTH, Window.MAX_HEIGHT, 0, 0)
        
    def start(self):
        for screen in self.screens:
            self.manager.start(screen)
    
    def update(self):
        for screen in self.screens:
            screen.update()
        for entity in EntityList.entity_list:
            entity.update()
        self.character.update()
        if WConio2.kbhit():
            (key, simbol) = WConio2.getch()
            self.character.handle_keys(simbol)
            if simbol.lower() == 'i':
                self.side_menu_screen.active = not self.side_menu_screen.active
                if not self.side_menu_screen.active:
                    self.side_menu_screen.on_exit()