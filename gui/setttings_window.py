from tkinter import *

raiz = Tk()

raiz.title("Traductor de Texto en Ventana")
raiz.resizable(False, False)
raiz.geometry("800x600")
#raiz.iconbitmap("icono.ico")

raiz.config(background="gray")

def Star_End():
    texto = btn_star["text"]
    if texto == "Star Translation":
        print("Iniciado")
        btn_star.config(text="End Translation")
    elif texto == "End Translation":
        print("Finalizado")
        btn_star.config(text="Star Translation")
        

btn_inicio = Label(raiz, text="Screen Translator")
btn_inicio.pack()

btn_star = Button(raiz, text="Star Translation", command= Star_End)
btn_star.pack()

raiz.mainloop()