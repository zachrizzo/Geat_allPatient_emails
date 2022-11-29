from shutil import move
from pynput.mouse import Button, Controller
import time
mouse = Controller()
sleep1 = time.sleep(5.5)
mouse.move(5, 0)
while True:
    for i in range(4):
        mouse.move(-55, 10)
        time.sleep(3)
        print("move")
    for i in range(4):
        mouse.move(55, -10)
        time.sleep(3)
        print("move")
    
    # mouse.move(55,-10)
        

