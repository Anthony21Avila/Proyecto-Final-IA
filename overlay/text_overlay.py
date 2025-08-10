from tkinter import Toplevel, Label
import win32gui, win32con
import pyautogui

#variables globales para que no tenga que crear el overlay cada vez
overlay = None
labels = []

def write_screen(opa, row, raiz):
    global overlay, labels

    if overlay is None:
        screen_w, screen_h = pyautogui.size()
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

    destry_labels()

    for r in row:
        overtext = Label(overlay, text=r["text"], bg="black", fg="white", font=("Arial", 17))
        overtext.place(x=r["x"], y=r["y"])
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