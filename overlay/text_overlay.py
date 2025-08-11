#Anthony Avila 23-SISN-2-002

from tkinter import Toplevel, Label
import win32gui, win32con
import pyautogui

#variables globales para que no tenga que crear el overlay cada vez
overlay = None
labels = []

def write_screen(opa, row, raiz):
    global overlay, labels

    screen_w, screen_h = pyautogui.size()
    if overlay is None:
        overlay = Toplevel(raiz)
        opacity = opa/100
        overlay.geometry(f"{screen_w}x{screen_h}+0+0")
        overlay.overrideredirect(True)
        overlay.wm_attributes("-topmost", True)
        overlay.wm_attributes("-transparentcolor", "#8a0000")
        overlay.wm_attributes('-alpha', opacity)
        overlay.resizable(False, False)
        overlay.config(background="#8a0000")
        
        hwnd = win32gui.GetParent(overlay.winfo_id())
        click_through(hwnd)
    
    width = int(screen_w * (2/3))
    overtext = Label(overlay, text=row, bg="black", fg="white", font=("Arial", 12), justify="left", anchor="nw", wraplength=width)
    
    x = (screen_w - width) // 2
    y= screen_h // 2
    
    overtext.update_idletasks()
    overtext.place(x=x, y=y, width=width)
    labels.append(overtext)

def destry_labels():
    global labels
    try: 
        for l in labels:
            l.destroy()
        labels.clear()
    except:
        pass

def click_through(hwnd):
    styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)