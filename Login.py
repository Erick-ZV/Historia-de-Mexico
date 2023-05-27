from tkinter import *
from Admin import Admin
from Conexion import *
import subprocess

database=DataBase()
root=Tk()
root.title("Login")
root.resizable(0, 0)
user_texto=StringVar()
pass_texto=StringVar()
backframe=Frame(root).grid(row=0, column=0)

back=PhotoImage(file='back.png')
Label(backframe, image=back).grid(row=0, column=0)

colorframe=(218, 165, 32)
initial_frame=Frame(root, width="600", height="350", bg='#%02x%02x%02x' % colorframe[:3],)
initial_frame.grid(row=0, column=0)

Label(initial_frame, text="Username:").grid(row=0, column=0, padx=10, pady=10 )
Label(initial_frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)
username=Entry(initial_frame, textvariable=user_texto).grid(row=0, column=1, sticky="e", padx=10, pady=10)
password=Entry(initial_frame, textvariable=pass_texto, show="*").grid(row=1, column=1, sticky="e", padx=10, pady=10)

def log_butt():
    user= user_texto.get()
    password=pass_texto.get()
    if database.check_user(user, password):
        print("Login exitoso")
        ruta='Mexico\Game.exe'
        subprocess.call(ruta)
    else:
        Label(initial_frame, text="Error de Credenciales", fg="red")

def sing_butt():
    user= user_texto.get()
    password=pass_texto.get()
    
    admin=Admin()
    admin.ventana()
    
        
login_button=Button(initial_frame, text="Login", command=log_butt).grid(row=2, column=0)
singup_button=Button(initial_frame, text="Admin", command=sing_butt).grid(row=2, column=1)
root.mainloop()
