from tkinter import Label, Tk, Button, DoubleVar, Scale, ttk

#Variables de Inicio
raiz = Tk()

raiz.title("Traductor de Texto en Ventana")
raiz.resizable(False, False)
raiz.geometry("800x600")
#raiz.iconbitmap("icono.ico")

raiz.config(background="gray")

#transparent_color = "black"
#raiz.wm_attributes('-transparentcolor', transparent_color)

#Funcion de Inicio
def Star_End():
    texto = btn_star["text"]
    if texto == "Star Translation":
        print("Iniciado")
        btn_star.config(text="End Translation")
    elif texto == "End Translation":
        print("Finalizado")
        btn_star.config(text="Star Translation")
        

#Label de Titulo
titule = Label(raiz, text="Screen Translator")
titule.pack()

#Combobox para idiomas
options = ["Inglish","Spanish", "French", "Chinese", "Japanese", "Korean", "German", "Russian"]
labelIn = Label(raiz, text="Select Original Lenguaje", bg="gray")
labelIn.pack(pady=(30, 0))
lengaujeIn = ttk.Combobox(raiz, values=options)
lengaujeIn.pack()

labelOut = Label(raiz, text="Select Destiny Lenguaje", bg="gray")
labelOut.pack(pady=(30, 0))
lengaujeOut = ttk.Combobox(raiz, values=options)
lengaujeOut.pack()

#Slider para opacidad del recuadro negro
background = Label(raiz, text="Background Opacity level", bg="gray")
background.pack(pady=(30, 0))
opacity = DoubleVar()
slider = Scale(raiz, from_=0, to=100, orient="horizontal", variable=opacity)
slider.pack()

#Boton de Inicio
btn_star = Button(raiz, text="Star Translation", command= Star_End)
btn_star.pack(pady=(30, 0))

raiz.mainloop()