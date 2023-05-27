from tkinter import *
from Conexion import *

database=DataBase()
root=Tk()
user_texto=StringVar()
pass_texto=StringVar()

initial_frame=Frame(root, width="600", height="350")
initial_frame.pack()

Label(initial_frame, text="Username:").grid(row=0, column=0, padx=10, pady=10 )
Label(initial_frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)
username=Entry(initial_frame, textvariable=user_texto).grid(row=0, column=1, sticky="e", padx=10, pady=10)
password=Entry(initial_frame, textvariable=pass_texto).grid(row=1, column=1, sticky="e", padx=10, pady=10)

def log_butt():
    user= user_texto.get()
    password=pass_texto.get()
    if database.into_user(user, password):
        Label(initial_frame, text="ALTA REALIZADA:", fg="blue").grid(row=2, column=0, padx=10, pady=10)
    else:
        Label(initial_frame, text="ALTA NO REALIZADA:", fg="red").grid(row=2, column=0, padx=10, pady=10)       
     
login_button=Button(initial_frame, text="Ingresar", command=log_butt).grid(row=3, column=0)
root.mainloop()
