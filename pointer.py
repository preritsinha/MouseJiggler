import pyautogui
import time
import random

pyautogui.FAILSAFE = False

def move_cursor(interval_seconds=5):
    print("Started")
    try:
        directions = [(50,0),(0,50),(-50,0),(0,-50)]
        current_direction = 0

        while True:
            dx,dy=directions[current_direction]
            duration = random.uniform(0.2,0.8)
            pyautogui.moveRel(dx,dy,duration=duration)
            current_direction=(current_direction+1)%len(directions)
            time.sleep(interval_seconds+random.uniform(-1,1))
    except KeyboardInterrupt:
        print("Exited")

if __name__=="__main__":
    move_cursor(2)