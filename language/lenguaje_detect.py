import mss.tools
import pyautogui
import pytesseract
from PIL import Image

#Funcion de captura de pantalla
def screenshot(monitor = int):
    src = mss.mss()
    sect_img = src.grab(src.monitors[monitor])
    img = Image.frombytes(mode="RGB", size=sect_img.size, data=sect_img.rgb)
    return img


def get_text(screen = int, lag = str):
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    img = screenshot(monitor=screen)
    text = pytesseract.image_to_data(img, lang=lag, output_type=pytesseract.Output.DICT)
    return text