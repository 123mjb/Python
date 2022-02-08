# importing modules
import pyautogui,keyboard
pyautogui.FAILSAFE=False
# returns a size object with
# width and height of the screen
print(pyautogui.size())
keyboard.wait('esc')
pyautogui.click(x=1919, y=1079, clicks=1, interval=0, button='left')

