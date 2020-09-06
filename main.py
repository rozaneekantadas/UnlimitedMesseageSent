import pyautogui
import time
message = 25

while message > 0:
    time.sleep(1)
    pyautogui.typewrite('I need you')
    pyautogui.press('enter')
    message = message -1