from tkinter import Toplevel, Label
import win32gui, win32con
import pyautogui

def write_screen(opa, row):
    screen_w, screen_h = pyautogui.size()
    overlay = Toplevel()
    opacity = opa/100
    overlay.geometry(f"{screen_w}x{screen_h}+0+0")
    overlay.overrideredirect(True)
    overlay.wm_attributes("-topmost", True)
    overlay.wm_attributes("-transparentcolor", "#8a0000")
    overlay.wm_attributes('-alpha', opacity)
    overlay.resizable(False, False)
    overlay.config(background="#8a0000")

    for r in row:
        overtext = Label(overlay, text=r["text"], bg="black")
        overtext.place(x=r["x"], y=r["y"])
        overtext.config(fg="white")

    hwnd = win32gui.GetParent(overlay.winfo_id())
    click_through(hwnd)

def click_through(hwnd):
    styles = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    styles |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, styles)