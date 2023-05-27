from tkinter import *
from Conexion import *

database=DataBase()
root=Tk()
user_texto=StringVar()

initial_frame=Frame(root, width="600", height="350")
initial_frame.pack()

Label(initial_frame, text="Username:", ).grid(row=0, column=0, padx=10, pady=10 )
username=Entry(initial_frame, textvariable=user_texto).grid(row=0, column=1, sticky="e", padx=10, pady=10)

def log_butt():
    user= user_texto.get()
    aviso=Label()
    if database.delete_user(user)==1:
        aviso.destroy()
        aviso=Label(initial_frame, text="Baja Realizada:", fg="Blue").grid(row=1, column=0, padx=10, pady=10 )
    else:
        aviso.destroy()
        aviso=Label(initial_frame, text="Baja NO Realizada:", fg="Red").grid(row=1, column=0, padx=10, pady=10 )
        
login_button=Button(initial_frame, text="Borrar", command=log_butt).grid(row=2, column=0)
root.mainloop()
