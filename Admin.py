from tkinter import *
from Conexion import *
import subprocess

class Admin:
    
    def ventana(self):
        
        raiz=Tk()
        raiz.title("Administrador")
        raiz.resizable(0, 0)
        initial_frame=Frame(raiz, width="600", height="350")
        initial_frame.pack()
        
        
        def registrar_but():
            raiz.destroy()
            ruta="C:\\Users\Erick\Desktop\Login-Game\Insert.py"
            subprocess.call(['python', ruta])
            self.ventana()
            
        registrar_button=Button(initial_frame, text="Registrar", width=10, height=10, command=registrar_but, font=20).grid(row=0, column=0)
        
        def listar_but():
            root=Tk()
            root.title("Lista de Usuarios")
            root.resizable(0, 0)
            initial_frame=Frame(root, width="600", height="350")
            initial_frame.pack()
            Label(initial_frame, text="ID:").grid(row=0, column=0, padx=10, pady=10 )
            Label(initial_frame, text="Username:").grid(row=0, column=1, padx=10, pady=10 )
            Label(initial_frame, text="Password:").grid(row=0, column=2, padx=10, pady=10)
            database=DataBase()
            users=database.check_all()
            for i in range (len(users)):
                for j in range(len(users[i])):
                    Label(initial_frame, text=users[i][j]).grid(row=i+1, column=j)
                
        listar_button=Button(initial_frame, text="Listar", width=10, height=10, command=listar_but, font=20).grid(row=0, column=1)
        def delete():
            raiz.destroy()
            ruta="C:\\Users\Erick\Desktop\Login-Game\Delete.py"
            subprocess.call(['python', ruta])
            self.ventana()
            
        borrar_button=Button(initial_frame, text="Borrar", width=10, height=10, command=delete, font=20).grid(row=0, column=2)
        raiz.mainloop()