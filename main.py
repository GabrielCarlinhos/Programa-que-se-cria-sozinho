import pyautogui
from random import randint

rand = randint(0,10000000)

pyautogui.PAUSE = 2
pyautogui.click(x=220, y=73)
pyautogui.write(f"main{rand}.py")
pyautogui.press("enter")

with open("script.txt","r") as file:
    script = file.read()
    pyautogui.write(script)
pyautogui.click(x=1830, y=48)




