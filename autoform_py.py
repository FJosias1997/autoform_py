import platform
import pyautogui
import time
import pandas as pd
import csv_bot

pyautogui.PAUSE = 1.5
browsers = ["firefox", "chrome", "edge", "safari", "opera"]

# Step 1: Identify the operating system
currentSystem = platform.system()

if currentSystem == "Darwin":  # macOS
    # Open Spotlight (shortcut: command + space)
    pyautogui.keyDown("command")
    pyautogui.press("space")
    pyautogui.keyUp("command")

    # search for the browser and open it
    pyautogui.write(browsers[0])  # Using Firefox as an example, but can be changed by just switching the index
    pyautogui.press("return")
    time.sleep(3)
elif currentSystem == "Windows":  # Windows
    pyautogui.press("win")
    pyautogui.write(browsers[2])  # Using Firefox as an example, but can be changed by just switching the index
    pyautogui.press("return")
    time.sleep(3)
elif currentSystem == "Linux":  # Linux
    pyautogui.press("super")
    pyautogui.write(browsers[0])  # Using Firefox as an example, but can be changed by just switching the index
    pyautogui.press("return")
    time.sleep(3)
else:
    print("Operating system not supported.")

# Call the function to automate the form filling using CSV data
csv_bot.csv_bot_filler()