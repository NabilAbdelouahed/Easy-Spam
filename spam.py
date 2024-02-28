import pyautogui
import time
time.sleep(5)
for i in range(100):
    f = open("spam text", "r")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(0.5)
