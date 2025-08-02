from tkinter import Label, Tk, Button, DoubleVar, Scale, ttk
from PyQt5 import QtWidgets
import sys

#Variables de Inicio
raiz = Tk()

raiz.title("Traductor de Texto en Ventana")
raiz.resizable(False, False)
raiz.geometry("800x600")
raiz.iconbitmap("icono.ico")
fondo = "#313131"
raiz.config(background=fondo)

#Variables de Estado
run = "paused"

#Funcion de Inicio
def Star_End():
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
options = ["Inglish (en)","Spanish (es)", "French (fr)", "Chinese (zh)", "Japanese (ja)", "Korean (ko)", "German (de)", "Russian (ru)"]
labelIn = Label(raiz, text="Select Original Lenguaje", bg=fondo)
labelIn.pack(pady=(30, 0))
lengaujeIn = ttk.Combobox(raiz, values=options)
lengaujeIn.pack()

labelOut = Label(raiz, text="Select Destiny Lenguaje", bg=fondo)
labelOut.pack(pady=(30, 0))
lengaujeOut = ttk.Combobox(raiz, values=options)
lengaujeOut.pack()

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

raiz.mainloop()