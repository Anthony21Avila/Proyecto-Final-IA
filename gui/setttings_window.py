from tkinter import Label, Tk, Button, DoubleVar, Scale, ttk
from PyQt5 import QtWidgets
import sys
import threading
import time
from overlay.text_overlay import background_opacity
from language.lenguaje_detect import get_text


#Variables de Inicio
raiz = Tk()

raiz.title("Traductor de Texto en Ventana")
raiz.resizable(False, False)
raiz.geometry("800x600")
raiz.iconbitmap("icono.ico")
fondo = "#313131"
raiz.config(background=fondo)
lang_code = ["eng","spa", "fra", "chi_sim", "jpn", "kor", "deu", "rus"]

#Variables de Estado
run = "paused"

#Funcion de Inicio
def Star_End():
    global run
    texto = btn_star["text"]
    if texto == "Star Translation":
        btn_star.config(text="End Translation")
        Status.config(fg="green", text="On")
        run = "running"

    elif texto == "End Translation":
        btn_star.config(text="Star Translation")
        Status.config(fg="red", text="Off")
        run = "paused"

#Funcion para contar monitores
def count_monitors():
    app = QtWidgets.QApplication(sys.argv)
    screen_count = app.desktop().screenCount()
    return screen_count
        

#Label de Titulo
titule = Label(raiz, text="Screen Translator")
titule.pack()

#Combobox para idiomas
options = ["English (en)","Spanish (es)", "French (fr)", "Chinese (zh)", "Japanese (ja)", "Korean (ko)", "German (de)", "Russian (ru)"]
labelIn = Label(raiz, text="Select Original Lenguaje", bg=fondo)
labelIn.pack(pady=(30, 0))
lenguajeIn = ttk.Combobox(raiz, values=options)
lenguajeIn.pack()

labelOut = Label(raiz, text="Select Destiny Lenguaje", bg=fondo)
labelOut.pack(pady=(30, 0))
lenguajeOut = ttk.Combobox(raiz, values=options)
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
monitorcb.pack()

#Slider para opacidad del recuadro negro
background = Label(raiz, text="Background Opacity level", bg=fondo)
background.pack(pady=(30, 0))
opacity = DoubleVar()
slider = Scale(raiz, from_=0, to=100, orient="horizontal", variable=opacity)
slider.pack()

#Boton de Inicio
btn_star = Button(raiz, text="Star Translation", command= Star_End)
btn_star.pack(pady=(30, 0))

#Estado
Status = Label(raiz, text="Off", bg="black", fg="Red")
Status.pack(pady=(70, 0))

def lang_select():
    valor = lenguajeIn.get() if lenguajeIn.get() else "English (en)"
    if valor in options:
        select = options.index(valor)
    else:
        select = 0  
    return select

def ocr_loop():
    def loop():
        while True:
            if run == "running":
                monitor_index = int(monitorcb.get()) if monitorcb.get() else 1
                l = lang_code[lang_select()] 
                background_opacity(slider.get())

                raw_text = get_text(screen=monitor_index, lag=l)
                if "text" in raw_text:
                    for i, txt in enumerate(raw_text["text"]):
                        if txt.strip() != "":
                            print("Texto capturado:", txt)
            time.sleep(2)
    threading.Thread(target=loop, daemon=True).start()

ocr_loop()