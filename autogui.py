import subprocess,sys,os
def install(package):
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("pyautogui")
install("keyboard")
import pyautogui,keyboard
pyautogui.FAILSAFE=False

def escape1():
  pyautogui.click(x=1919, y=1079, clicks=1, interval=0, button='left')
  # sys.exit()
def killl():
  sys.exit()
print(pyautogui.size())
# keyboard.wait('esc')
keyboard.add_hotkey('Esc', lambda: escape1())
keyboard.add_hotkey('ctrl+shift+a', lambda: killl())
while True:
  continue

  


