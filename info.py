from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import pygame
from bd import bd

class Info():
    def __init__(self, root):
        self.root = root
        self.root.title("Informacion Mascotas")
        self.root.geometry("1080x720+400+60")
        self.root.resizable(False, False)

        self.Ventana()

    def Ventana(self):
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        frameIzquierdo = Frame(root, bg="pink")
        frameIzquierdo.grid(column=0, row=0, sticky="nsew")
        frameDerecho = Frame(root, bg="green")
        frameDerecho.grid(column=1, row=0, sticky="nsew")

        #---------------------lado derecho------------------------------

        labelPet = Label(frameIzquierdo, text="Kevin Alberto Medina Cardenas")
        labelPet.pack(pady=15)

        image = Image.open("imagenes/ProfileIcon.png")
        image = image.resize((130, 130))
        photo = ImageTk.PhotoImage(image)
        labelImage = customtkinter.CTkLabel(frameIzquierdo, image=photo, text="")
        labelImage.pack(pady=15)

        image2 = Image.open("imagenes/codigo-qr.png")
        image2 = image2.resize((130, 130))
        photoQR = ImageTk.PhotoImage(image2)

        labelName = Label(frameIzquierdo, text="Dueño")
        labelName.pack(pady=15)
        entryName = customtkinter.CTkEntry(frameIzquierdo, height=50, width=250)
        entryName.pack(pady=15)

        labelCont = Label(frameIzquierdo, text="Contacto")
        labelCont.pack(pady=15)
        entryCont = customtkinter.CTkEntry(frameIzquierdo, height=50, width=250)
        entryCont.pack(pady=15)

        #------------------------------------lado izquierdo----------------------------------------

        labelInfo = LabelFrame(frameDerecho, text="Informacion")
        labelInfo.pack(fill="x")
        labelInfo.columnconfigure(0, weight=1)
        labelInfo.columnconfigure(1, weight=1)

        labelVacunas = Label(labelInfo, text="Vacunas administradas")
        labelVacunas.grid(column=0, row=0)
        vacunasText = Text(labelInfo, width=30, height=7)
        vacunasText.grid(column=1, row=0, pady=15, padx=10)

        labelAlergias = Label(labelInfo, text="Alergias")
        labelAlergias.grid(column=0, row=1)
        alergiasText = Text(labelInfo, width=30, height=7)
        alergiasText.grid(column=1, row=1, pady=15, padx=10)

        labelPadecimientos = Label(labelInfo, text="Padecimientos")
        labelPadecimientos.grid(column=0, row=2)
        padecimientosText = Text(labelInfo, width=30, height=7)
        padecimientosText.grid(column=1, row=2, pady=15, padx=10)

        labelQR = LabelFrame(frameDerecho, text="Generación")
        labelQR.pack(fill="both")
        labelQR.columnconfigure(0, weight=1)
        labelQR.columnconfigure(1, weight=1)

        labelGenerar = Label(labelQR, text="Presiona para generar tu Codigo QR -----> ")
        labelGenerar.grid(column=0, row=0)
        btnQR = Button(labelQR, image=photoQR, width=130, height=130)
        btnQR.grid(column=1, row=0)




if __name__ == "__main__":
    root = Tk()
    app = Info(root)
    root.mainloop()        
