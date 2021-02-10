from tkinter import *

def iniciar_sesion():
    ventana2 = Tk()
    ventana2.geometry("500x200")
    ventana2.resizable(0, False)
    ventana2.mainloop()


ventana1 = Tk()
ventana1.geometry("500x200")
ventana1.resizable(0, False)
# ventana1.config()
fondo1 = photoImage(file="Fondo1.gif")
etiqueta_fondo1 = Label(ventana1, image=fondo1).place(x=0, y=0)
Label(ventana1, text="Usted ya esta registrado?").grid(
    row=1, column=0, sticky=E, padx=175
)
boton = Button(ventana1, text="Iniciar sesion", command=iniciar_sesion).grid(
    row=2, column=0
)
Label(ventana1, text="Usted no esta registrado?").grid(row=3, column=0)
boton = Button(ventana1, text="Registrarse", command=iniciar_sesion).grid(
    row=4, column=0
)
ventana1.mainloop()