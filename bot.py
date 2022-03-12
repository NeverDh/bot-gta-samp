import pyautogui
import time

def andar():
    time.sleep(10)
    pyautogui.keyDown('w')
    pyautogui.keyDown('a')
    pyautogui.keyUp('w')
    pyautogui.keyDown('s')
    pyautogui.keyUp('a')
    pyautogui.keyDown('d')
    pyautogui.keyUp('s')
    pyautogui.keyDown('w')
    pyautogui.keyUp('d')
    pyautogui.keyUp('w')
    time.sleep(5)
    caixinha()



def caixinha():
    pyautogui.hotkey('t')
    time.sleep(1)
    pyautogui.write('/caixinha')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1200)
    identificar()


def login():
    time.sleep(2)
    posLog = pyautogui.locateOnScreen("alvos/entrar.png")
    x = posLog.left
    y = posLog.top

    pyautogui.click(x+25, y+15, duration= 2)
    time.sleep(20)
    identificar()



def identificar():
    time.sleep(5)
    posLog = pyautogui.locateOnScreen("alvos/entrar.png")
    if posLog != None:
        login()
    else:
        andar()


identificar()

