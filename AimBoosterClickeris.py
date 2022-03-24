from pyautogui import *
import pyautogui
import time
import win32api, win32con
import keyboard

#Paspaudimo funkcija
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #Atleidimo delay kad nefailintu paspaudimas
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


pyautogui.alert('Spauskite OK kad ijungtumėte clickeri! \n\n(Išjungti su Q)')

#Scripto išjungimas su Q
while keyboard.is_pressed('q') == False:
#Suranda taikini ir atlieka click() funkcija
    taskas = pyautogui.locateCenterOnScreen(r'C:\Users\Dovydas\Desktop\stuff\python\AimBoosterClickeris\taskas.png', grayscale=True, confidence=0.9, region= (300,200,640,500))
    if taskas != None:
        x, y = taskas
        click(x, y)
        sleep(0.1) #Delay kad spėtu pranykti paspaustas taikinys
    else:
        sleep(0.0)

if keyboard.is_pressed('q') == True:
    pyautogui.alert("Clickeris išjungtas!")