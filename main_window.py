from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from registro import RegistroApp



###--------------------------------------------Ventana Principal------------------------------------------###
class main_window(ctk.CTk):

    def daniel_tonto(self):
        print("pendejo")
    
    def kevin_tonto(self):
        print("tonto")

    def abrir_registro(self):
        app = Toplevel(ventana)
        registro = RegistroApp(app)
        registro.mainloop()  # Asegúrate de que la clase RegistroApp tiene su propio mainloop si es necesario

    def __init__(self):
        super().__init__()
        self.title("Selecciona tu Mascota")
        self.geometry("1080x720+400+60")

        # Menu de hamburguesa en la esquina superior izquierda
        self.menu_button = ctk.CTkButton(self, text="☰", command=self.toggle_menu, width=80, fg_color="lightgray", corner_radius=10)
        self.menu_button.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="nw")

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
        self.search_frame.grid(row=0, column=1, columnspan=2, padx=20, pady=10, sticky="ew")

        # una mejora que le agregue a la barra de busqueda para que este centrada y no abarque todo el ancho
        self.search_entry = ctk.CTkEntry(self.search_frame, placeholder_text="Buscar Dueño", width=300)
        self.search_entry.pack(padx=10, pady=5)

        # lista de mascotas en la columna o frame izquierdo
        self.list_frame = ctk.CTkFrame(self)
        self.list_frame.grid(row=1, column=1, padx=(20, 0), pady=10, sticky="nsew")

        # canvas para barra desplazadora jsajsja
        self.canvas = ctk.CTkCanvas(self.list_frame)
        self.scrollbar = ctk.CTkScrollbar(self.list_frame, orientation="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # agregar las imagenes
        self.pet_data = [
            ("imagenes/conejo_icon.jpg", "Nombre dueño\nNombre mascota"),
            ("imagenes/gato_icon.jpg", "Nombre dueño\nNombre mascota"),
            ("imagenes/hamster_icon.jpg", "Nombre dueño\nNombre mascota"),
            ("imagenes/nutria_icon.jpg", "Nombre dueño\nNombre mascota"),
            ("imagenes/perro_icon.jpg", "Nombre dueño\nNombre mascota"),
            ("imagenes/tortuga_icon.jpg", "Nombre dueño\nNombre mascota")
        ]

        # crear botones con las imagenes de las mascotas, no se como ponerle a esta parte perdon
        self.pet_buttons = []
        for img_path, text in self.pet_data:
            image = Image.open(img_path).resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            self.create_pet_item(photo, text)

        # Columna derecha con imagen y texto (con imagen inicial del perrito)
        self.right_frame = ctk.CTkFrame(self, fg_color="#FFF8E1", width=300, height=400)  # Tamaño fijo
        self.right_frame.grid(row=1, column=2, padx=20, pady=10, sticky="nsew")
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
        self.name_label = ctk.CTkLabel(self.content_frame, text="", font=("Arial", 20), anchor='center')
        self.name_label.pack(pady=(0, 5))

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

        # Configuracion de la disposicion de la ventana, en realidad no esta funcionando esta parte no se porque, en teoria era para poder hacer que la lista de animales abaracara todo el ancho
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def create_pet_item(self, image, text):
        """Crea un item de mascota en la lista como botón."""
        pet_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=None)
        pet_frame.pack(padx=5, pady=15)

        # Crear un boton con la imagen de la mascota
        pet_button = ctk.CTkButton(
            pet_frame,
            image=image,
            text="",
            width=100,
            height=100,
            fg_color=None,
            command=lambda img=image, txt=text: self.display_pet_info(img, txt)
        )
        pet_button.pack(side="left", padx=5)

        # Etiqueta con el nombre de la mascota y el dueño
        pet_label = ctk.CTkLabel(pet_frame, text=text, font=("Arial", 20), fg_color=None)
        pet_label.pack(side="left", padx=10)

    def display_pet_info(self, image, text):
        """Muestra la información de la mascota seleccionada en la columna derecha."""
        self.selected_image_label.configure(image=image)
        self.selected_image_label.image = image

        # Mostrar la información en la columna derecha
        self.name_label.configure(text="Nombre de Mascota")
        self.id_label.configure(text="MO123")
        self.owner_label.configure(text="Dueño: \nKevin Alberto Medina Cardenas\n")
        self.contact_label.configure(text="Contacto: \nexample@gmail.com")

    def show_full_info(self):
        """Mostrar información completa de la mascota seleccionada.""" 
        open_info_window()  # Llama a la ventana de información completa

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
        self.label_popOut.pack(fill="both", pady = (2, 10), padx="10")
        
        #boton donde si damos 'si' se cierra la sesion, en teoria una vez se cierre te regresa a la pantalla de login
        self.cerrar = ctk.CTkButton(
            self.popout, 
            text="Si", 
            command=self.close_session, 
            fg_color="red", 
            corner_radius=10,
            width=150
        )
        self.cerrar.pack(fill="x" ,padx=(2,10) , side="left")
        
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