from tkinter import Label, Tk, Button, DoubleVar, Scale, ttk
from PyQt5 import QtWidgets
import sys
from overlay.text_overlay import write_screen, destry_labels
from language.lenguaje_detect import get_text
from language.gpt_translator import translate_openai


#Variables de Inicio
raiz = Tk()

raiz.title("Traductor de Texto en Ventana")
raiz.resizable(False, False)
raiz.geometry("300x500")
raiz.iconbitmap("icono.ico")
fondo = "#313131"
raiz.config(background=fondo)
lang_code = ["eng","spa", "fra", "deu"]

#Funcion para iniciar el OCR
def ocr():
    monitor_index = int(monitorcb.get())
    l = lang_code[lang_select()]
    text = get_text(screen=monitor_index, lag=l)
    if text.strip() != "":
        translated = translate_openai(text, lenguajeOut.get())
        write_screen(slider.get(), translated, raiz)

#Funcion para contar monitores
def count_monitors():
    app = QtWidgets.QApplication(sys.argv)
    screen_count = app.desktop().screenCount()
    return screen_count
        

#Label de Titulo
titule = Label(raiz, text="Screen Translator")
titule.pack()

#Combobox para idiomas
options = ["English (en)","Spanish (es)", "French (fr)", "German (de)"]
labelIn = Label(raiz, text="Select Original Lenguaje", bg=fondo)
labelIn.pack(pady=(30, 0))
lenguajeIn = ttk.Combobox(raiz, values=options)
lenguajeIn.current(0)
lenguajeIn.pack()

labelOut = Label(raiz, text="Select Destiny Lenguaje", bg=fondo)
labelOut.pack(pady=(30, 0))
lenguajeOut = ttk.Combobox(raiz, values=options)
lenguajeOut.current(0)
lenguajeOut.pack()

#Seleccionar monitor
monitor_Num = []
monitors = count_monitors()
i=0
while i in range(monitors):
    i += 1
    monitor_Num.append(i)
monitorlb = Label(raiz, text="Select Monitor", bg=fondo)
monitorlb.pack(pady=(30, 0))
monitorcb = ttk.Combobox(raiz, values=monitor_Num)
monitorcb.current(0)
monitorcb.pack()

#Slider para opacidad del recuadro negro
background = Label(raiz, text="Background Opacity level", bg=fondo)
background.pack(pady=(30, 0))
opacity = DoubleVar()
slider = Scale(raiz, from_=0, to=100, orient="horizontal", variable=opacity)
slider.pack()

#Boton de Inicio
btn_star = Button(raiz, text="Translation", command= ocr)
btn_star.pack(pady=(30, 0))

#Boton para limpiar pantalla
btn_clean = Button(raiz, text="Clean Screen", command= destry_labels)
btn_clean.pack(pady=(10, 0))

def lang_select():
    valor = lenguajeIn.get()
    if valor in options:
        select = options.index(valor)
    else:
        select = 0  
    return select