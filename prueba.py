from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from registro import RegistroApp
from bd import bd
import traceback
from info import Info

###--------------------------------------------           Ventana Principal                 ------------------------------------------###
class main_window(ctk.CTk):
    
    base = bd()
    data = base.Obtener_info_lista()
    base.Cerrar()

    tam = len(data)

    def abrir_registro(self):
        app = Toplevel(ventana)
        registro = RegistroApp(app)
        registro.mainloop()
        self.update()
        
    def obtener_info_completa(self):
        base = bd()
        data = base.obtener_info_derecha()
        base.Cerrar()
        return data
        
    def obtener_info_lista(self):
        base = bd()
        data = base.Obtener_info_lista()
        base.Cerrar()
        return data
    
    def obtener_info(self):
        base = bd()
        data = base.Obtener_info_lista()
        base.Cerrar()
        return data
    
    def updateOne(self):
        print("update entrando")
        self.lista_mascotas = self.obtener_info()
        tam2 = len(self.lista_mascotas)
        if(int(self.tam) < int(tam2)):
            print("refrescando vista")
            new = self.lista_mascotas[-1]
            imagen3 = "imagenes/" + new[1]
            texto = new[2] + "\n" + new[3]
            image = Image.open(imagen3).resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.create_pet_item(photo, texto, new[0])
            self.tam += 1
        else:
            print(self.tam, tam2)
        
    def update(self):    
        for pet_id, img_icon, nombre, mascota in self.lista_mascotas:
            imagen3 = "imagenes/" + img_icon
            texto = nombre + "\n" + mascota
            image = Image.open(imagen3).resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.create_pet_item(photo, texto, pet_id)

    def __init__(self):
        super().__init__()
        self.id = 0
        self.title("Selecciona tu Mascota")
        self.geometry("1080x720+400+60")
        
        # Configuracion de la disposicion de la ventana, en realidad no esta funcionando esta parte no se porque, en teoria era para poder hacer que la lista de animales abaracara todo el ancho
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Menu de hamburguesa en la esquina superior izquierda
        self.menu_button = ctk.CTkButton(self, text="☰", command=self.toggle_menu, width=80, fg_color="lightgray", corner_radius=10)
        self.menu_button.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="nw")
        
        # Barra de color azul en la parte inferior
        self.register_frame = ctk.CTkFrame(self, fg_color="lightblue")
        self.register_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky="nsew")

        # Configurar el grid del frame para centrar el contenido
        self.register_frame.grid_columnconfigure(0, weight=1)

        # Frame que contendrá los botones, centrado en la barra azul
        button_frame = ctk.CTkFrame(self.register_frame, fg_color="lightblue")
        button_frame.grid(row=0, column=0, pady=10)

        # Botón "Registrar"
        self.register_button = ctk.CTkButton(
            button_frame,
            text="  Registrar ",
            width=70,
            height=50,
            fg_color="orange",
            corner_radius=25,
            command=lambda: self.abrir_registro()
        )
        self.register_button.grid(row=0, column=0, padx=5)  # Pequeño espacio a la izquierda y derecha

        # Botón "Refrescar"
        self.boton_refresh = ctk.CTkButton(
            button_frame,
            fg_color="orange",
            text="Refrescar",
            width=40,
            height=50,
            corner_radius=25,
            command=lambda: self.updateOne()
        )
        self.boton_refresh.grid(row=0, column=1, padx=5)  # Pequeño espacio a la izquierda y derecha

        # Frame del menu despegable de hamburguesa
        self.menu_frame = ctk.CTkFrame(self, fg_color="white")
        self.menu_frame.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="nw")
        self.menu_frame.grid_remove()  # Comenzar oculto
        
        # botones aun sin funcionalidad del menu
        self.about_button = ctk.CTkButton(self.menu_frame, text="Sobre nosotros", command=self.show_about, width=200)
        self.about_button.pack(pady=5)

        self.help_button = ctk.CTkButton(self.menu_frame, text="Ayuda", command=self.show_help, width=200)
        self.help_button.pack(pady=5)

        #A este wey ya le di funcionalidad
        self.logout_button = ctk.CTkButton(self.menu_frame, text="Cerrar sesión", command=self.popOut_cerrarsesion, width=200)
        self.logout_button.pack(pady=5)

        # Barra de busqueda en la parte superior generalmente en el centro(la mejorare despues)
        self.search_frame = ctk.CTkFrame(self, fg_color="white")
        self.search_frame.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="nsew")

        # una mejora que le agregue a la barra de busqueda para que este centrada y no abarque todo el ancho
        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Buscar Dueño", width=300)
        self.search_entry.pack(padx=10, pady=5)
        
        #frame mascotas
        self.mascotas_frame = ctk.CTkFrame(self, width=300)
        self.mascotas_frame.grid(row = 1, column = 1, padx=0, pady = 0 ,sticky ="nsew")
        
        self.lista_mascotas = self.obtener_info_lista()

        self.update()
        
        # frame de la columna derecha con informacion y configuraciones
        self.right_frame = ctk.CTkFrame(self, fg_color="#FFF8E1", width=300)
        self.right_frame.grid(row=1, column=2, padx=10, pady=0, sticky="nsew")
        self.right_frame.grid_propagate(False)

        # Contenedor de imagen y texto, sin modificar tamaño
        self.content_frame = ctk.CTkFrame(self.right_frame, width=300, height=400)
        self.content_frame.pack_propagate(False)
        self.content_frame.pack(expand=True)
        
        # Columna derecha con imagen y texto (con imagen inicial del perrito)
        self.right_frame = ctk.CTkFrame(self, fg_color="#FFF8E1", width=300)  # Tamaño fijo
        self.right_frame.grid(row=1, column=2, padx=0, pady=0, sticky="nsew")
        self.right_frame.grid_propagate(False)  # Evitar que el frame cambie de tamaño

        # Contenedor de imagen y texto, sin modificar tamaño
        self.content_frame = ctk.CTkFrame(self.right_frame, width=300, height=400)
        self.content_frame.pack_propagate(False)
        self.content_frame.pack(expand=True)

        # agregar la imagen inicial del perrito
        initial_image = Image.open("imagenes/noseleccion.jpg").resize((300, 300))
        self.default_photo = ImageTk.PhotoImage(initial_image)
        
        self.text_label = ctk.CTkLabel(self.right_frame, text="Selecciona tu mascota", font=("Arial", 16))
        self.text_label.pack(pady=(0, 10))

        # Etiqueta de imagen
        self.selected_image_label = ctk.CTkLabel(self.content_frame, image=self.default_photo, text="")
        self.selected_image_label.pack(pady=15)
        
        # Etiquetas de informacion
        self.nombre_mascota = ctk.CTkLabel(self.content_frame, text="", font=("Arial", 20), anchor='center')
        self.nombre_mascota.pack(pady=(0, 5))

        self.id_label = ctk.CTkLabel(self.content_frame, text="", font=("Arial", 20), anchor='center')
        self.id_label.pack(pady=(0, 5))

        # Frame para dueño y contacto
        self.info_frame = ctk.CTkFrame(self.content_frame, fg_color="lightgray", corner_radius=10)
        self.info_frame.pack(pady=(10, 10), padx=10, fill="both", expand=True)

        self.owner_label = ctk.CTkLabel(self.info_frame, text="", font=("Arial", 16), anchor='w')
        self.owner_label.pack(pady=(5, 0))

        self.contact_label = ctk.CTkLabel(self.info_frame, text="", font=("Arial", 16), anchor='w')
        self.contact_label.pack(pady=(5, 10))

        # Boton "Ver informacion completa"
        self.full_info_button = ctk.CTkButton(self.content_frame, text="Ver información completa", command=self.show_full_info)
        self.full_info_button.pack(pady=(10, 10))

        # Boton de registro en la parte inferior
        self.register_frame = ctk.CTkFrame(self, fg_color="lightblue")
        self.register_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky="ew")

        # Boton redondo
        self.register_button = ctk.CTkButton(
            self.register_frame,
            text="Registrar",
            width=50,
            height=50,
            fg_color="orange",
            corner_radius=25,
            command=lambda: self.abrir_registro()
        )
        self.register_button.pack(pady=10)

    def create_pet_item(self, image, text):
        """Crea un item de mascota en la lista como botón."""
        pet_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=None)
        pet_frame.pack(padx=5, pady=15)
        # Boton "Ver informacion completa"-----------------------------------------------------------------------------------------------------------
        self.full_info_button = ctk.CTkButton(self.content_frame, text="Ver información completa", command=lambda: self.show_full_info())
        self.full_info_button.pack(pady=(10, 10))
        
        self.lista_info_completa = self.obtener_info_completa()
        
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def on_canvas_resize(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.frame_window, width=canvas_width)

    def create_pet_item(self, image, text, pet_id):
        pet_frame = ctk.CTkFrame(self.mascotas_frame, fg_color=None)
        pet_frame.grid(row=self.mascotas_frame.grid_size()[1], column=0, padx=5, pady=15, sticky="ew")

        # Configurar el ancho de la columna
        self.mascotas_frame.grid_columnconfigure(0, weight=1)

        # Crear un boton con la imagen de la mascota
        pet_button = ctk.CTkButton(
            pet_frame,
            image=image,
            text="",
            width=100,
            height=100,
            fg_color=None,
            command=lambda img=image, txt=text, id=pet_id: self.display_pet_info(img, id)
        )
        pet_button.pack(side="left", padx=5)
        pet_label = ctk.CTkLabel(pet_frame, text=text, font=("Arial", 20), fg_color=None)
        pet_label.pack(side="left", padx=10)
        
    #muestra la info de la parte derecha
    def display_pet_info(self, image, pet_id):
        self.selected_image_label.configure(image=image)
        self.selected_image_label.image = image
        try:
            self.lista = self.obtener_info_completa()
            for tupla in self.lista:
                id, nombre, mascota, contacto = tupla
                self.id = id
                if id == pet_id:
                    self.nombre_mascota.configure(text=mascota)
                    self.id_label.configure(text=id)
                    self.owner_label.configure(text="Dueño: \n" + nombre + "\n")
                    self.contact_label.configure(text="Contacto: \n" + contacto)
                    break  # Terminar el bucle una vez se haya encontrado la mascota
        except Exception as e:
            print("Hubo un error: ", str(e))
            print(traceback.format_exc())

    def show_full_info(self):
        ven = Toplevel(ventana)
        app = Info(ven, self.id)
        app.mainloop()
        

    def toggle_menu(self):
        """Alternar visibilidad del menú desplegable.""" 
        if self.menu_frame.winfo_ismapped():
            self.menu_frame.grid_remove()
            self.grid_columnconfigure(0, weight=0)
        else:
            self.menu_frame.grid()
            self.grid_columnconfigure(0, weight=0)
            
    #el pop out para cerrar la sessin, ya es funcional solo falta un poco mas de dise;o, 
    def popOut_cerrarsesion(self):
        self.popout = ctk.CTkToplevel()
        self.popout.geometry("300x150+700+300")
        self.popout.resizable(False, False)
        
        #con esto para que salga siempre enfrente
        self.popout.lift()
        self.popout.attributes("-topmost", True)
        
        #el label del pop out
        self.label_popOut = ctk.CTkLabel(self.popout, text="Estas seguro de que deseas cerrar sesion?", font=("Arial", 20), wraplength=250)
        self.label_popOut.pack(fill="both", pady = (10, 10), padx="10")
        
        #boton donde si damos 'si' se cierra la sesion, en teoria una vez se cierre te regresa a la pantalla de login
        self.cerrar = ctk.CTkButton(
            self.popout, 
            text="Si", 
            command=self.close_session, 
            fg_color="red", 
            corner_radius=10,
            width=150
        )
        self.cerrar.pack(fill="x" ,padx=(10,10) , side="left")
        
        #este es pa que nos e cierre
        self.no_cerrar = ctk.CTkButton(   
            self.popout, 
            text="No", 
            command=self.no_close_session, 
            fg_color="green", 
            corner_radius=10, 
            width=150
        )
        self.no_cerrar.pack(fill="x" ,padx=(10,2) , side="left")

    def show_about(self):
        #--Mostrar información sobre la aplicacion.--# 
        ctk.CTkMessagebox.show_info("Sobre nosotros", "Este es un programa para gestionar mascotas.")

    #--Mostrar ayuda.--# 
    def show_help(self):
        ctk.CTkMessagebox.show_info("Ayuda", "Aquí puedes buscar y registrar mascotas.")

    #--Boton para cerrar secion--#
    def close_session(self):
        self.destroy()
        
    def no_close_session(self):
        self.popout.destroy()
        
ventana = main_window()
ventana.mainloop()