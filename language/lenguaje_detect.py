import mss.tools
import pyautogui

#Funcion de captura de pantalla
def screenshot(monitor = int):
    src = mss.mss()
    filename = src.shot(mon=monitor, output='fullscreen.png')
    filename

screenshot(1)