from mss import mss
import pytesseract
from PIL import Image, ImageOps
from langid import classify, set_languages

#Funcion de captura de pantalla
def screenshot(monitor = int):
    src = mss()
    sect_img = src.grab(src.monitors[monitor])
    img = Image.frombytes(mode="RGB", size=sect_img.size, data=sect_img.rgb)
    return img

#Funcion para tomar el texto dle fondo
def get_text(screen = int, lag = str):
    pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
    img = screenshot(monitor=screen)
    img = preprocess_image(img)
    text = pytesseract.image_to_data(img, lang=lag, output_type=pytesseract.Output.DICT)
    return text

#Procesar la imagen para mejorar el resultado
def preprocess_image(img):
    img = ImageOps.grayscale(img)
    img = img.point(lambda x: 0 if x < 140 else 255) 
    return img

#Filtro de Idioma y caracteres 
def languaje_detect(txt, code):
    set_languages([code])
    try:
        if not txt or len(txt.strip()) < 4:
            return False
        else:
            lang_text, prob = classify(txt)
            if lang_text == code and prob >= 6:
                return True
            else:
                return False
    except:
        return False