from tkinter import Label, Tk, Button, DoubleVar, Scale, ttk
from PyQt5 import QtWidgets
import sys
import threading
import time
from overlay.text_overlay import write_screen, destry_labels
from language.lenguaje_detect import get_text, languaje_detect
from language.gpt_translator import translate_openai
from queue import Queue


#Variables de Inicio
raiz = Tk()

raiz.title("Traductor de Texto en Ventana")
raiz.resizable(False, False)
raiz.geometry("300x600")
raiz.iconbitmap("icono.ico")
fondo = "#313131"
raiz.config(background=fondo)
lang_code = ["eng","spa", "fra", "chi_sim", "jpn", "kor", "deu", "rus"]
code = ["en","es", "fr", "zh", "ja", "ko", "de", "ru"]

#Variables de Estado
run = "paused"

#Cola para recibir en el hilo principal datos (y evitar que se pete el programa)
queue = Queue()

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
btn_star = Button(raiz, text="Star Translation", command= Star_End)
btn_star.pack(pady=(30, 0))

#Boton para limpiar pantalla
btn_clean = Button(raiz, text="Clean Screen", command= destry_labels)
btn_clean.pack(pady=(10, 0))

#Estado
Status = Label(raiz, text="Off", bg="black", fg="Red")
Status.pack(pady=(50, 0))

def lang_select():
    valor = lenguajeIn.get()
    if valor in options:
        select = options.index(valor)
    else:
        select = 0  
    return select

#Loop que controla el el estado del OCR
def ocr_loop():
    def loop():
        resultado = []
        while True:
            if  run == "running":
                monitor_index = int(monitorcb.get())
                l = lang_code[lang_select()]
                c = code[lang_select()]

                #Conseguimos el texto de la pantalla y hacemos unas verificaciones para comprobar si debe o no traducirse
                text = get_text(screen=monitor_index, lag=l)
                for i, txt in enumerate(text["text"]):
                    conf = int(text["conf"][i])
                    if isinstance(txt, str) and txt.strip() != "" and conf >= 50:
                        lang_val = languaje_detect(txt, c)
                        if lang_val == True:
                            translated = translate_openai(txt.strip(), lenguajeOut.get())
                            resultado.append({"text": translated, "x": text["left"][i], "y": text["top"][i]})
                queue.put(resultado)    
            time.sleep(5)

    threading.Thread(target=loop, daemon=True).start()

#Funcion para enviar los datos al overlay en el hilo principal. A tkinter no le gusta abrir ventana en hilos a parte
def data_queue():
    #Se usa try para que siempre lo haga, pero solo podra cuando hayan datos en la cola
    try:
        resultado = queue.get_nowait() #para sacar y quitar datos de la cola
        write_screen(slider.get(), resultado, raiz)
    except:
        pass
    raiz.after(4000, data_queue) #para que se llame sola despues de 5 segundos

ocr_loop()
data_queue()