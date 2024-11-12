from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk
import pygame
from bd import bd

class RegistroApp:

    def __init__(self, root):
        self.root = root
        self.root.geometry("400x600+800+140")
        self.root.resizable(False, False)

        pygame.mixer.init()
        
        # Atributos y configuración inicial
        self.circles = []
        self.active_color = "orange"
        self.inactive_color = "white"
        self.num_tabs = 4
        self.current_index = 0
        self.color1 = "#82bce9"
        self.imagenes = ["gato_icon.jpg", "perro_icon.jpg", "nutria_icon.jpg", "hamster_icon.jpg", 
                        "conejo_icon.jpg", "lagarto_icon.jpg", "tortuga_icon.jpg", "ProfileIcon.png"]
        
        self.profile = "imagenes/ProfileIcon.png"
        self.currentImage = ""
        self.entryV = StringVar()
        self.entryA = StringVar()
        self.entryP = StringVar()

        self.Register()

    def VerificarPosicion(self, btn):
        if(self.current_index != 0):
            btn.config(state="active", bg="orange")
        else:
            btn.config(state="disabled", bg="orange")

    def Confirmacion(self):
        confirmacion = messagebox.askyesno("Guardar cambios", "Estas seguro que la informacion es correcta")
        if confirmacion:
            self.GuardarInfo()
            self.root.destroy()
        else:
            self.current_index -= 1

    def GuardarInfo(self):
            base = bd()
            if self.currentImage != "":
                base.AgregarMascota(self.entryName.get(), self.entryPet.get(), self.entryAddress.get(), self.entryV.get(), self.entryA.get(), self.entryP.get(), self.currentImage)
            else:
                base.AgregarMascota(self.entryName.get(), self.entryPet.get(), self.entryAddress.get(), self.entryV.get(), self.entryA.get(), self.entryP.get(), "ProfileIcon.png")

            data = base.ObtenerInfoMascotas()
            print(data)
            base.Cerrar()


    def update_indicator(self, canvas):
        for i, circle in enumerate(self.circles):
            color = self.active_color if i == self.current_index else self.inactive_color
            canvas.itemconfig(circle, fill=color)

    def next_tab(self, canvas):
        if self.Validar():
            self.current_index = (self.current_index + 1)
            if(self.current_index >= 4):
                self.Confirmacion()
            else:
                self.update_indicator(canvas)
        else:
            aviso = messagebox.showinfo("Rellenar campos", "Tiene que rellenar los campos obligatorios")


    def previous_tab(self, canvas):
        if(self.current_index != 0):
            self.current_index = (self.current_index - 1)
            self.update_indicator(canvas)
    
    def Validar(self):
        if  self.entryName.get() != "" and self.entryPet.get() != "" and self.entryAddress.get() != "":
            return True
        else:
            return False

    def Register(self):
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)

        # FRAMES DIVIDIDOS
        frameTop = Frame(self.root, relief="groove", border=10, borderwidth=5)
        frameTop.grid(column=0, row=0, sticky="nsew")

        frameMid = Frame(self.root, relief="flat")
        frameMid.grid(column=0, row=1, sticky="nsew")

        frameBot = Frame(self.root, relief="flat")
        frameBot.grid(column=0, row=2, sticky="nsew")

        style = ttk.Style()
        style.layout("TNotebook.Tab", [])

        tab_control_top = ttk.Notebook(frameTop)
        self.tab1 = Frame(tab_control_top, bg=self.color1)
        self.tab2 = Frame(tab_control_top, bg="#f9b7b2")
        self.tab3 = Frame(tab_control_top, bg="#d26193")
        self.tab4 = Frame(tab_control_top, bg="#90ac8e")
        tab_control_top.add(self.tab1, text='Informacion personal')
        tab_control_top.add(self.tab2, text='Vacunas administradas')
        tab_control_top.add(self.tab3, text='Alergias')
        tab_control_top.add(self.tab4, text='Padecimientos')
        tab_control_top.pack(expand=1, fill='both')

        tab_control_mid = ttk.Notebook(frameMid)
        self.tab1_mid = Frame(tab_control_mid)
        self.tab2_mid = Frame(tab_control_mid)
        self.tab3_mid = Frame(tab_control_mid)
        self.tab4_mid = Frame(tab_control_mid)
        tab_control_mid.add(self.tab1_mid, text='Informacion personal')
        tab_control_mid.add(self.tab2_mid, text='Vacunas administradas')
        tab_control_mid.add(self.tab3_mid, text='Alergias')
        tab_control_mid.add(self.tab4_mid, text='Padecimientos')
        tab_control_mid.pack(expand=1, fill='both')

        # DISEÑO DEL FRAME TOP
        labelTitulo = Label(self.tab1, text="Informacion personal", bg=self.color1, fg="white")
        labelTitulo.pack(pady=10)

        # INFORMACION PERSONAL
        frameSelector = Frame(self.tab1)
        frameSelector.pack()

        image = Image.open(self.profile)
        image = image.resize((130, 130))
        photo = ImageTk.PhotoImage(image)
        self.image2 = Image.open("imagenes/pencil.jpg")
        self.image2 = self.image2.resize((50, 50))
        self.photo2 = ImageTk.PhotoImage(self.image2) 


        LabelImageProfile = customtkinter.CTkLabel(frameSelector, image=photo, text="", bg_color=self.color1)
        LabelImageProfile.pack()
        btnSelector = Button(self.tab1, image=self.photo2, width=50, height=50, command=lambda: Selector())
        btnSelector.place(x=50, y=70)

        self.entryName = customtkinter.CTkEntry(self.tab1_mid, placeholder_text="Nombre del dueño", height=50)
        self.entryName.pack(pady=15, padx=60, fill="x")

        self.entryPet = customtkinter.CTkEntry(self.tab1_mid, placeholder_text="Nombre de la mascota", height=50)
        self.entryPet.pack(pady=15, padx=60, fill="x")

        self.entryAddress = customtkinter.CTkEntry(self.tab1_mid, placeholder_text="Domicilio", height=50)
        self.entryAddress.pack(pady=15, padx=60, fill="x")

        # VACUNAS ADMINISTRADAS
        imageVacunas = Image.open("imagenes/vacunas_icon.png")
        imageVacunas = imageVacunas.resize((130, 130))
        photoVacunas = ImageTk.PhotoImage(imageVacunas)

        labelTab2 = Label(self.tab2, text="Vacunas administradas")
        labelTab2.pack(pady=10)
        LabelImage = customtkinter.CTkLabel(self.tab2, image=photoVacunas, text="")
        LabelImage.pack()

        self.tab2_mid.columnconfigure(0, weight=1)
        self.tab2_mid.columnconfigure(1, weight=1)
        self.tab3_mid.columnconfigure(0, weight=1)
        self.tab3_mid.columnconfigure(1, weight=1)
        self.tab4_mid.columnconfigure(0, weight=1)
        self.tab4_mid.columnconfigure(1, weight=1)

        lbVacunas = Label(self.tab2_mid, text="Introduzca las vacunas que se conoce han sido adminisitradas a la mascota", justify="center", wraplength=250, font=("Verdana",14) )
        lbVacunas.grid(column=0, columnspan=2, row=0, pady=15, padx=10)
        self.entryT2 = customtkinter.CTkEntry(self.tab2_mid, placeholder_text="Vacunas", height=70, width=250, textvariable=self.entryV).grid(column=0, columnspan=2, row=1, pady=15, padx=10)

        lbAlergias = Label(self.tab3_mid, text="En caso de tenerlas, introduzca las alergias que se conoce tiene la mascota", justify="center", wraplength=250, font=("Verdana",14))
        lbAlergias.grid(column=0, columnspan=2, row=0, pady=15, padx=10)
        self.entryT3 = customtkinter.CTkEntry(self.tab3_mid, placeholder_text="Opcional", height=70, width=250, textvariable=self.entryA).grid(column=0, columnspan=2, row=1, pady=15, padx=10)

        lbPadecimientos = Label(self.tab4_mid, text="En caso de tener, introduzca los padecimientos que se conoce tiene la mascota", justify="center", wraplength=250, font=("Verdana",14) )
        lbPadecimientos.grid(column=0, columnspan=2, row=0, pady=15, padx=10)
        self.entryT4 = customtkinter.CTkEntry(self.tab4_mid, placeholder_text="Otras (especifique)", height=70, width=250, textvariable=self.entryP).grid(column=0, columnspan=2, row=1, pady=15, padx=10)

        # ALERGIAS-----------------------------------------------

        imageAlergias = Image.open("imagenes/alergias_icon.png")
        imageAlergias = imageAlergias.resize((130, 130))
        photoAlergias = ImageTk.PhotoImage(imageAlergias)

        labelTab3 = Label(self.tab3, text="Alergias")
        labelTab3.pack(pady=10)
        LabelImage = customtkinter.CTkLabel(self.tab3, image=photoAlergias, text="")
        LabelImage.pack()

        # PADECIMIENTOS------------------------------------------

        imagePadecimientos = Image.open("imagenes/padecimientos_icon.png")
        imagePadecimientos = imagePadecimientos.resize((130, 130))
        photoPadecimientos = ImageTk.PhotoImage(imagePadecimientos)

        labelTab4 = Label(self.tab4, text="Padecimientos")
        labelTab4.pack(pady=10)
        LabelImage = customtkinter.CTkLabel(self.tab4, image=photoPadecimientos, text="")
        LabelImage.pack()

        # DISEÑO DEL FRAME BOTTTTTTTTTT-----------------------------------------------------------------------------

            # BOTONES DE AVANCE

        def next_info():
            tab_control_top.select(self.current_index)
            tab_control_mid.select(self.current_index)

        frameBtn = Frame(frameBot)
        frameBtn.pack(side="bottom", pady=20)
        frameBtn.columnconfigure(0, weight=1)
        frameBtn.columnconfigure(1, weight=1)

        btnPrevius = Button(frameBtn, text="Anterior", state="disabled", command=lambda: (self.previous_tab(canvas), next_info(), self.VerificarPosicion(btnPrevius)), bg="orange", width=15, height=2, relief="groove", border=10, borderwidth=5)
        btnPrevius.grid(column=0, row= 0, padx=10)
        
        btnNext = Button(frameBtn, text="Siguiente",command=lambda: (self.next_tab(canvas), next_info(), self.VerificarPosicion(btnPrevius)), bg="orange", width=15, height=2, relief="groove", border=10, borderwidth=5)
        btnNext.grid(column=1, row= 0, padx=10)
        
        # INDICADORES DE AVANCE

        canvas = Canvas(frameBot, width=200, height=50)
        canvas.pack(side="bottom")

        for i in range(self.num_tabs):
            x = 35 + i * 40
            circle = canvas.create_oval(x, 10, x + 20, 30, fill=self.inactive_color, outline="black")
            self.circles.append(circle)

        self.update_indicator(canvas)

        def CambiarPerfil(num, window, label_image):
            global profile
            global sonidos
            self.currentImage = self.imagenes[num]
            profile = self.imagenes[num]
            image = Image.open("imagenes/" + profile)
            image = image.resize((130, 130))
            photo = ImageTk.PhotoImage(image)
            label_image.configure(image=photo)
            label_image.image = photo  #
            window.destroy()

        def Selector():
            selector = Toplevel()
            selector.geometry("350x350")
            selector.resizable(False,False)

            frameImagenes = Frame(selector)
            frameImagenes.pack(fill="both")

            # iconos ---------------------------------------------
            image_icon = Image.open("imagenes/gato_icon.jpg")
            image_icon = image_icon.resize((80, 80))
            icon_gato = ImageTk.PhotoImage(image_icon)

            image_icon = Image.open("imagenes/perro_icon.jpg")
            image_icon = image_icon.resize((80, 80))
            icon_perro = ImageTk.PhotoImage(image_icon)

            image_icon = Image.open("imagenes/nutria_icon.jpg")
            image_icon = image_icon.resize((80, 80))
            icon_nutria = ImageTk.PhotoImage(image_icon)

            image_icon = Image.open("imagenes/tortuga_icon.jpg")
            image_icon = image_icon.resize((80, 80))
            icon_tortuga = ImageTk.PhotoImage(image_icon)

            image_icon = Image.open("imagenes/lagarto_icon.jpg")
            image_icon = image_icon.resize((80, 80))
            icon_iguana = ImageTk.PhotoImage(image_icon)

            image_icon = Image.open("imagenes/conejo_icon.jpg")
            image_icon = image_icon.resize((80, 80))
            icon_conejo = ImageTk.PhotoImage(image_icon)

            image_icon = Image.open("imagenes/hamster_icon.jpg")
            image_icon = image_icon.resize((80, 80))
            icon_hamster = ImageTk.PhotoImage(image_icon)

            image_icon = Image.open("imagenes/cancel.png")
            image_icon = image_icon.resize((80, 80))
            icon_noseleccion = ImageTk.PhotoImage(image_icon) 

            btn1 = customtkinter.CTkButton(frameImagenes, image=icon_gato, width=80, height=80, text="", command=lambda: CambiarPerfil(0, selector, LabelImageProfile)).grid(column=0, row=0)
            btn2 = customtkinter.CTkButton(frameImagenes, image=icon_perro, width=80, height=80, text="", command=lambda: CambiarPerfil(1, selector, LabelImageProfile)).grid(column=1, row=0, padx=10, pady=10)
            btn3 = customtkinter.CTkButton(frameImagenes, image=icon_nutria, width=80, height=80, text="", command=lambda: CambiarPerfil(2, selector, LabelImageProfile)).grid(column=2, row=0, padx=10, pady=10)
            btn4 = customtkinter.CTkButton(frameImagenes, image=icon_hamster, width=80, height=80, text="", command=lambda: CambiarPerfil(3, selector, LabelImageProfile)).grid(column=0, row=1, padx=10, pady=10)
            btn5 = customtkinter.CTkButton(frameImagenes, image=icon_conejo, width=80, height=80, text="", command=lambda: CambiarPerfil(4, selector, LabelImageProfile)).grid(column=1, row=1, padx=10, pady=10)
            btn6 = customtkinter.CTkButton(frameImagenes, image=icon_iguana, width=80, height=80, text="", command=lambda: CambiarPerfil(5, selector, LabelImageProfile)).grid(column=2, row=1, padx=10, pady=10)
            btn7 = customtkinter.CTkButton(frameImagenes, image=icon_tortuga, width=80, height=80, text="", command=lambda: CambiarPerfil(6, selector, LabelImageProfile)).grid(column=0, row=2, padx=10, pady=10)
            btn7 = customtkinter.CTkButton(frameImagenes, image=icon_noseleccion, width=80, height=80, text="", command=lambda: CambiarPerfil(7, selector, LabelImageProfile)).grid(column=1, row=2, padx=10, pady=10)

if __name__ == "__main__":
    root = Tk()
    app = RegistroApp(root)
    root.mainloop()        
