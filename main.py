from tkinter import *
from registro import RegistroApp

tk = Tk()

def abrir_registro():
    app = Toplevel(tk)
    registro = RegistroApp(app)
    registro.mainloop()  # Asegúrate de que la clase RegistroApp tiene su propio mainloop si es necesario

btn = Button(tk, text="Ingresar", command=abrir_registro)
btn.pack()

tk.mainloop()