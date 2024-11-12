from tkinter import *
import customtkinter
from PIL import Image, ImageTk
from bd import bd
import qrcode

class Info():

    def __init__(self, root, id):
        self.root = root
        self.root.title("Informacion Mascotas")
        self.root.geometry("1080x720+400+60")
        self.root.resizable(False, False)
        self.id = id

        self.Ventana()

    def GenerarQR(self):
        #generador de qr
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data("https://www.youtube.com/watch?v=GBIIQ0kP15E")
        qr.make(fit=True)
        img = qr.make_image(fill = "black", back_color = "white")
        img.save("qr.png")

    def InfoMascota(self):
        base = bd()
        info = base.ObtenerInfo(self.id)
        print(info)
        base.Cerrar()
        self.labelPet.config(text=info[2])
        self.entryName.insert(INSERT, info[1])
        self.entryCont.insert(INSERT, info[3])
        self.vacunasText.insert(INSERT, info[4])
        self.alergiasText.insert(INSERT, info[5])
        self.padecimientosText.insert(INSERT, info[6])
        

    def Ventana(self):
        print("EL ID ES:", self.id)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        frameIzquierdo = Frame(self.root, bg="#A8EAF9", relief="groove", border=2, borderwidth=2)
        frameIzquierdo.grid(column=0, row=0, sticky="nsew")
        frameDerecho = Frame(self.root, relief="groove", border=2, borderwidth=2)
        frameDerecho.grid(column=1, row=0, sticky="nsew")

        #---------------------lado izquierdo------------------------------

        frameContenedor = Frame(frameIzquierdo, bg="#A8EAF9")
        frameContenedor.pack(expand=True, fill="none")

        self.labelPet = Label(frameContenedor, text="Kevin Alberto Medina Cardenas", font=("Verdana",15))
        self.labelPet.pack(pady=15)
        self.labelID = Label(frameContenedor, text="MO123", font=("Verdana",13))
        self.labelID.pack(pady=15)

        self.image = Image.open("imagenes/ProfileIcon.png")
        self.image = self.image.resize((150, 150))
        self.photo = ImageTk.PhotoImage(self.image)
        self.labelImage = customtkinter.CTkLabel(frameContenedor, image=self.photo, text="")
        self.labelImage.pack(pady=15)

        image2 = Image.open("imagenes/codigo-qr.png")
        image2 = image2.resize((130, 130))
        photoQR = ImageTk.PhotoImage(image2)

        self.root.photoQR = photoQR

        image3 = Image.open("imagenes/pencil.jpg")
        image3 = image3.resize((50, 50))
        photo3 = ImageTk.PhotoImage(image3) 

        self.root.photo3 = photo3

        labelName = Label(frameContenedor, text="Dueño", font=("Verdana",15))
        labelName.pack(pady=15)

        frameName = Frame(frameContenedor, bg="#A8EAF9")
        frameName.pack()
        frameName.columnconfigure(0, weight=1)
        frameName.columnconfigure(1, weight=1)
        btnName = Button(frameName, width=50, height=50, image=photo3)
        btnName.grid(column=0, row=0, padx= 10)
        self.entryName = customtkinter.CTkEntry(frameName, height=59, width=250)
        self.entryName.grid(column=1, row=0, pady=15)

        labelCont = Label(frameContenedor, text="Contacto", font=("Verdana",15))
        labelCont.pack(pady=15)

        frameCont = Frame(frameContenedor, bg="#A8EAF9")
        frameCont.pack()
        frameCont.columnconfigure(0, weight=1)
        frameCont.columnconfigure(1, weight=1)
        btnCont = Button(frameCont, width=50, height=50, image=photo3)
        btnCont.grid(column=0, row=0, padx= 10)
        self.entryCont = customtkinter.CTkEntry(frameCont, height=59, width=250)
        self.entryCont.grid(column= 1, row= 0, pady=15)

        #------------------------------------lado derecho----------------------------------------

        imageV = Image.open("imagenes/vacunas_icon.png")
        imageV = imageV.resize((50, 50))
        photoV = ImageTk.PhotoImage(imageV)

        imageP = Image.open("imagenes/padecimientos_icon.png")
        imageP = imageP.resize((50, 50))
        photoP = ImageTk.PhotoImage(imageP)

        imageA = Image.open("imagenes/alergias_icon.png")
        imageA = imageA.resize((50, 50))
        photoA = ImageTk.PhotoImage(imageA)

        labelInfo = Frame(frameDerecho)
        labelInfo.pack(fill="x", padx=10, pady=10)
        labelInfo.columnconfigure(0, weight=1)
        labelInfo.columnconfigure(1, weight=1)

        labelVacunas = customtkinter.CTkLabel(labelInfo, text="       Vacunas administradas", image=photoV, compound="left", width=100, anchor="center", font=("Verdana",18))
        labelVacunas.grid(column=0, row=0, sticky= "nsew", padx= 20)
        self.vacunasText = Text(labelInfo, width=30, height=7)
        self.vacunasText.grid(column=1, row=0, pady=15, padx=10)

        labelAlergias = customtkinter.CTkLabel(labelInfo, text="             Alergias                ", image=photoA, compound="left", width=100, font=("Verdana",18))
        labelAlergias.grid(column=0, row=1, sticky= "nsew", padx= 20)
        self.alergiasText = Text(labelInfo, width=30, height=7)
        self.alergiasText.grid(column=1, row=1, pady=15, padx=10)

        labelPadecimientos = customtkinter.CTkLabel(labelInfo, text="          Padecimientos         ", image=photoP, compound="left", width=100, font=("Verdana",18))
        labelPadecimientos.grid(column=0, row=2, sticky= "nsew", padx= 20)
        self.padecimientosText = Text(labelInfo, width=30, height=7)
        self.padecimientosText.grid(column=1, row=2, pady=15, padx=10)

        labelQR = Frame(frameDerecho)
        labelQR.pack(fill="both", padx=10)
        labelQR.columnconfigure(1, weight=1)
        labelQR.columnconfigure(0, weight=1)

        labelGenerar = Label(labelQR, text="Presiona para generar tu Codigo QR        -----> ", font=("Verdana",10, "bold"))
        labelGenerar.grid(column=0, row=0)
        btnQR = Button(labelQR, image=photoQR, width=130, height=130, command=lambda: self.GenerarQR())
        btnQR.grid(column=1, row=0)

        self.InfoMascota()

if __name__ == "__main__":
    root = Tk()
    app = Info(root)
    root.mainloop()        
