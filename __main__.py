import os 
import cursor
from settings.settings import Timer
from screen.main_screen import MainScreen
cursor.hide()
os.system("cls")

main_screen = MainScreen()

timer = 0
main_screen.start()
while (True):
    if (timer % 200000 == 0):
        Timer.tick += 1
        timer = 0
        main_screen.update()
    
    if (Timer.tick >= 300000):
        Timer.tick = 0

    timer += 1