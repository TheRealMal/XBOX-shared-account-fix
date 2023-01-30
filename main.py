import keyboard
import os
import time

time.sleep(30)
os.system("taskkill /f /im explorer.exe")
while True:
    try:
        if keyboard.is_pressed('home'):
            os.system("start explorer.exe")
            break
    except:
        break