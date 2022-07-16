import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
def menuPantalla():
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("gato.ico")

    image = PhotoImage(file="gato.gif")
    image = image.subsample(5, 5)
    label = Label(image=image)
    label.pack()
    Label(text="Acceso al sistema", bg="slate gray", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(text="").pack()
    Button(text="Iniciar Sesión", height="3", width="30").pack()
    Label(text="").pack()
    Button(text="Registrarse", height="3", width="30").pack()

    pantalla.mainloop()

def inicioSesion():
    global pantalla1
    pantalla1=Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("gato.ico")

    Label(pantalla1, text="Por favor ingrese su usuario y contraseña acontinuacion").pack()
    Label(pantalla1, text="").pack()

    global nombreUsuarioVerify
    global contrasenaUsuarioVerify

    nombreUsuarioVerify=StringVar()
    contrasenaUsuarioVerify=StringVar()

    global nombreUsuarioEntry
    global contrasenaUsuarioEntry

    Label(pantalla1, text="Usuario").pack()
    nombreUsuarioEntry=Entry(pantalla1,textvariable=nombreUsuarioVerify)
    nombreUsuarioEntry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasenaUsuarioEntry = Entry(pantalla1, textvariable=contrasenaUsuarioVerify)
    contrasenaUsuarioEntry.pack()
    Label(pantalla1).pack()

