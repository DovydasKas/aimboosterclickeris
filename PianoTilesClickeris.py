from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con



#Pirma eile(nuo kaires) X:  472 Y:  430 RGB: (142, 199, 254)
#Antra eile X:  540 Y:  436 RGB: ( 83, 176, 210)
#trecia eile X:  606 Y:  423 RGB: (159, 214, 255)
#ketvirta eile X:  677 Y:  431 RGB: (136, 168, 251)



#Paspaudimo funkcija
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #time.sleep(0.01)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(472,430) [2] == 1:
        click(472,430)

    elif pyautogui.pixel(540,436) [2] == 1:
        click(540,436)

    elif pyautogui.pixel(606,423) [2] == 1:
        click(606,423)

    elif pyautogui.pixel(677,431) [2] == 1:
        click(677,431)

    elif pyautogui.pixel(472,430) [2] == 2:
        click(472,430)

    elif pyautogui.pixel(540,436) [2] == 2:
        click(540,436)

    elif pyautogui.pixel(606,423) [2] == 2:
        click(606,423)

    elif pyautogui.pixel(677,431) [2] == 2:
        click(677,431) 
    

    elif pyautogui.pixel(472,430) [0] == 0:
        click(472,430)

    elif pyautogui.pixel(540,436) [0] == 0:
        click(540,436)

    elif pyautogui.pixel(606,423) [0] == 0:
        click(606,423)

    elif pyautogui.pixel(677,431) [0] == 0:
        click(677,431)

    elif pyautogui.pixel(472,430) [0] == 1:
        click(472,430)

    elif pyautogui.pixel(540,436) [0] == 1:
        click(540,436)

    elif pyautogui.pixel(606,423) [0] == 1:
        click(606,423)

    elif pyautogui.pixel(677,431) [0] == 1:
        click(677,431)

    elif pyautogui.pixel(472,430) [0] == 2:
        click(472,430)

    elif pyautogui.pixel(540,436) [0] == 2:
        click(540,436)

    elif pyautogui.pixel(606,423) [0] == 2:
        click(606,423)

    elif pyautogui.pixel(677,431) [0] == 2:
        click(677,431)

    elif pyautogui.pixel(472,430) [0] == 17:
        click(472,430)

    elif pyautogui.pixel(540,436) [0] == 17:
        click(540,436)

    elif pyautogui.pixel(606,423) [0] == 17:
        click(606,423)

    elif pyautogui.pixel(677,431) [0] == 17:
        click(677,431)

    elif pyautogui.pixel(472,430) [0] == 15:
        click(472,430)

    elif pyautogui.pixel(540,436) [0] == 15:
        click(540,436)

    elif pyautogui.pixel(606,423) [0] == 15:
        click(606,423)

    elif pyautogui.pixel(677,431) [0] == 15:
        click(677,431)

    elif pyautogui.pixel(472,430) [0] == 18:
        click(472,430)

    elif pyautogui.pixel(540,436) [0] == 18:
        click(540,436)

    elif pyautogui.pixel(606,423) [0] == 18:
        click(606,423)

    elif pyautogui.pixel(677,431) [0] == 18:
        click(677,431)

    elif pyautogui.pixel(472,430) [0] == 20:
        click(472,430)

    elif pyautogui.pixel(540,436) [0] == 20:
        click(540,436)

    elif pyautogui.pixel(606,423) [0] == 20:
        click(606,423)

    elif pyautogui.pixel(677,431) [0] == 20:
        click(677,431)

    elif pyautogui.pixel(472,430) [0] == 32:
        click(472,430)

    elif pyautogui.pixel(540,436) [0] == 32:
        click(540,436)

    elif pyautogui.pixel(606,423) [0] == 32:
        click(606,423)

    elif pyautogui.pixel(677,431) [0] == 32:
        click(677,431)

    elif pyautogui.pixel(472,430) [2] == 132:
        click(472,430)

    elif pyautogui.pixel(540,436) [2] == 132:
        click(540,436)

    elif pyautogui.pixel(606,423) [2] == 132:
        click(606,423)

    elif pyautogui.pixel(677,431) [2] == 132:
        click(677,431)

