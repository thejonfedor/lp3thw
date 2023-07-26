
import pyautogui as gui
import random
import time

cursor_coordinates = gui.position()
afk_counter = 0
xy = ""
sleepTime = 2

while True: 

    if gui.position() == cursor_coordinates:
        afk_counter += 1

    else:
        afk_counter = 0
        cursor_coordinates = gui.position()

    if afk_counter > 5:
        x = random.randint(400,1800)    
        y = random.randint(200,900)
        moveTime = round(random.uniform(0.1,1.5),1)
        sleepTime = random.randint(1,7)
        gui.moveTo(x, y, moveTime)
        xy = f"-- Positions X: {x} and Y: {y} and Move Time: {moveTime} and Sleep Time: {sleepTime}"
        cursor_coordinates = gui.position()
    
    if afk_counter > 0 and afk_counter % 15 == 0:
        gui.hotkey('command', 'tab')

    print(f'AFK Counter: {afk_counter} {xy}')
    time.sleep(sleepTime)
    xy = ""