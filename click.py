import time
import pyautogui

time.sleep(5)
print(pyautogui.position())

# While running this script, hover over the desired location and wait for 5 seconds.
# The script will print the current mouse coordinates (x, y) in the console.
# Use these coordinates in the csv_bot.py script on the line 30 where it says:
# pyautogui.click