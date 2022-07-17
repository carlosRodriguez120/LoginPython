import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql


def menuPantalla():
    global pantalla
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
    Button(text="Iniciar Sesión", height="3", width="30", command=inicioSesion).pack()
    Label(text="").pack()
    Button(text="Registrarse", height="3", width="30", command=registro).pack()

    pantalla.mainloop()


def inicioSesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesion")
    pantalla1.iconbitmap("gato.ico")

    Label(pantalla1, text="Por favor ingrese su usuario y contraseña acontinuacion", bg="slate gray", fg="white",
          width="300", height="3", font=("calibri", 12)).pack()
    Label(pantalla1, text="").pack()

    global nombreUsuarioVerify
    global contrasenaUsuarioVerify

    nombreUsuarioVerify = StringVar()
    contrasenaUsuarioVerify = StringVar()

    global nombreUsuarioEntry
    global contrasenaUsuarioEntry

    Label(pantalla1, text="Usuario").pack()
    nombreUsuarioEntry = Entry(pantalla1, textvariable=nombreUsuarioVerify)
    nombreUsuarioEntry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasenaUsuarioEntry = Entry(pantalla1, show="*", textvariable=contrasenaUsuarioVerify)
    contrasenaUsuarioEntry.pack()
    Label(pantalla1).pack()
    Button(pantalla1, text="iniciar sesion", command=validacionDatos).pack()


def registro():
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("gato.ico")

    global nombreUsuarioEntry1
    global contraseñaUsusarioEntry1

    nombreUsuarioEntry1 = StringVar()
    contraseñaUsusarioEntry1 = StringVar()
    Label(pantalla2, text="por fabor ingrese un usuario y una contraseña \n para el registro al sistema",
          bg="slate gray", fg="white", width="300", height="3", font=("calibri", 15)).pack()
    Label(pantalla2, text=" ")

    Label(pantalla2, text="Usuario").pack()
    nombreUsuarioEntry1 = Entry(pantalla2)
    nombreUsuarioEntry1.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="contraseña").pack()
    contraseñaUsusarioEntry1 = Entry(pantalla2, show="*")
    contraseñaUsusarioEntry1.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=insertarDatos).pack()


def insertarDatos():
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bd2"
    )
    fcursor = bd.cursor()
    sql = "INSERT INTO login (usuario, contrasena) VALUES ('{0}', '{1}')".format(nombreUsuarioEntry1.get(),
                                                                                 contraseñaUsusarioEntry1.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="registro exitoso", title="aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="registro NO exitoso", title="aviso")
    bd.close()


def validacionDatos():
    bd = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="bd2"
    )
    fcursor = bd.cursor()
    fcursor.execute(
        "SELECT contrasena FROM login WHERE usuario='" + nombreUsuarioVerify.get() + "' and contrasena='" + contrasenaUsuarioVerify.get() + "'")
    if fcursor.fetchall():
        messagebox.showinfo("inicio de sesión correcto", message="usuario y contraseña correcta")
        pantallaInicio()

    else:
        messagebox.showinfo("inicio de sesión incorrecto", message="usuario y contraseña incorrecta NO")
        bd.close()


def pantallaInicio():
    global pantalla3

    pantalla3 = Toplevel(pantalla)
    pantalla3.geometry("300x380")
    pantalla3.title("welcome")
    pantalla3.iconbitmap("gato.ico")
    Label(pantalla3, text="bienvenido, gracias por iniciar sesion", bg="slate gray", fg="white", width="300",
          height="3", font=("calibri", 12)).pack()

    image1 = PhotoImage(file="gato.gif")
    image1 = image1.subsample(1, 1)
    label1 = Label(image=image1)
    label1.pack()




menuPantalla()
