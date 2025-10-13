import time
import pyautogui

#Important: After running this script, quickly place the mouse pointer over the desired position and wait for 5 seconds.
#The result will be printed in the terminal. And then, copy into the Line 28 from csv_bot.py

time.sleep(5)
print(pyautogui.position())

pyautogui.scroll(200)